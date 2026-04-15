from collections import defaultdict

class Solution:
    def unique_segments(self, intervals):
        events = defaultdict(int)

        # build events
        for s, e in intervals:
            events[s] += 1
            events[e + 1] -= 1   # +1 because intervals are inclusive

        # sweep
        active = 0
        prev = None
        result = []

        for x in sorted(events):
            if prev is not None and active == 1:
                result.append([prev, x - 1])

            active += events[x]
            prev = x

        return result