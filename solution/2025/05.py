from solution.base import Base

class Solution(Base):
    year = 2025
    day = "05"

    fresh = []
    ranges = {}
    items = []

    def _parse_input(self, data):
        lines = data.splitlines()
        using_fresh = False
        for line in lines:
            if using_fresh:
                self.items.append(int(line))
            else:
                if line == '':
                    using_fresh = True
                else:
                    (start, end) = line.split('-')
                    if int(start) in self.ranges:
                        self.ranges[int(start)] = max(self.ranges[int(start)], int(end))
                    else:
                        self.ranges[int(start)] = int(end)

    def _isfresh(self, item):
        for start, end in self.ranges.items():
            if start <= item <= end:
                return True
        return False

    def _part1(self):
        output = 0
        for item in self.items:
            if self._isfresh(item):
                output += 1
        return output

    def _part2(self):
        keys = sorted(self.ranges)
        output = 0
        cur = 0
        for key in keys:
            start = max(key, cur)
            end = self.ranges[key]
            if start <= end:
                output += end - start + 1
                cur = end + 1
        return output
