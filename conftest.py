import importlib.util
import inspect
import pathlib
import pytest


GREEN = "\033[32m"
RED = "\033[31m"
DIM = "\033[2m"
RESET = "\033[0m"


class _Recorder:
    def __init__(self):
        self.last_args = None
        self.last_kwargs = None
        self.last_result = None
        self.called = False


def _load_callable(sol_path):
    spec = importlib.util.spec_from_file_location(sol_path.stem, sol_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    if hasattr(mod, "solution"):
        return mod.solution

    if hasattr(mod, "Solution"):
        instance = mod.Solution()
        methods = [
            m for m, _ in inspect.getmembers(instance, predicate=inspect.ismethod)
            if not m.startswith("_")
        ]
        if len(methods) != 1:
            raise RuntimeError(
                f"{sol_path}: expected exactly one public method on Solution, "
                f"found {methods}"
            )
        return getattr(instance, methods[0])

    raise RuntimeError(
        f"{sol_path}: must define `solution` function or `Solution` class"
    )


@pytest.fixture
def solution(request):
    sol_path = pathlib.Path(request.fspath).parent / "solution.py"
    fn = _load_callable(sol_path)
    rec = _Recorder()
    request.node._solution_rec = rec

    def wrapper(*args, **kwargs):
        rec.called = True
        rec.last_args = args
        rec.last_kwargs = kwargs
        rec.last_result = fn(*args, **kwargs)
        return rec.last_result

    return wrapper


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when != "call":
        return
    rec = getattr(item, "_solution_rec", None)
    if rec is None or not rec.called:
        return
    tr = item.config.pluginmanager.getplugin("terminalreporter")
    if tr is None:
        return

    tag = f"{GREEN}PASS{RESET}" if report.passed else f"{RED}FAIL{RESET}"
    name = item.name
    if "[" in name and name.endswith("]"):
        name = name[name.index("[") + 1 : -1]

    args = rec.last_args or ()
    if len(args) == 1 and not rec.last_kwargs:
        in_repr = repr(args[0])
    elif rec.last_kwargs:
        in_repr = f"args={args} kwargs={rec.last_kwargs}"
    else:
        in_repr = repr(args)

    tr.write_line(
        f"  {tag}  {name}  {DIM}in={RESET}{in_repr}  {DIM}out={RESET}{rec.last_result!r}"
    )
