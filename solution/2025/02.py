import re
from solution.base import Base

class Solution(Base):
    year = 2025
    day = "02"

    def _parse_input(self, data):
        ranges = (x.split('-') for x in data.split(','))
        input = []
        for x in ranges:
            input.append((int(x[0]), int(x[1])+1))
        return input

    def _part1(self):
        re_two = re.compile(r'^(.+)\1$')
        ret = 0
        for x in self.input:
            for i in range(*x):
                if re_two.fullmatch(str(i)):
                    ret += i
        return ret

    def _part2(self):
        re_multiple = re.compile(r'^(.+)(\1){1,}$')
        ret = 0
        for x in self.input:
            for i in range(*x):
                if re_multiple.fullmatch(str(i)):
                    ret += i
        return ret
