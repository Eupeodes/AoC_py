from solution.base import Base

class Solution(Base):
    year = 2025
    day = "05"

    ranges = {}
    items = []

    def _parse_input(self, data):
        lines = data.splitlines()
        using_fresh = False
        ranges = {}
        for line in lines:
            if using_fresh:
                self.items.append(int(line))
            else:
                if line == '':
                    using_fresh = True
                else:
                    (start, end) = line.split('-')
                    if int(start) in ranges:
                        ranges[int(start)] = max(ranges[int(start)], int(end))
                    else:
                        ranges[int(start)] = int(end)
        keys = sorted(ranges)
        curend = 0
        start = 0
        curstart = 0
        for key in keys:
            end = ranges[key]
            if key <= curend:
                self.ranges[curstart] = max(self.ranges[curstart], end)
                end = max(curend, end)
            else:
                self.ranges[key] = end
                curend = end
                curstart = key

    def _isfresh(self, item):
        for start, end in self.ranges.items():
            if start > item:
                return False
            if end >= item:
                return True
        return False

    def _part1(self):
        output = 0
        for item in self.items:
            if self._isfresh(item):
                output += 1
        return output

    def _part2(self):
        output = 0
        for start, end in self.ranges.items():
            output += end - start + 1
        return output
