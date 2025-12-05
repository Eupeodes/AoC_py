from solution.base import Base

class Solution(Base):
    year = 2025
    day = "03"

    def parse_input(self, data):
        return data.splitlines()

    def part1(self):
        ret = 0
        for bank in self.input:
            ret += _get_yoltage(bank, 2)
        return ret

    def part2(self):
        ret = 0
        for bank in self.input:
            ret += _get_yoltage(bank, 12)
        return ret


def _get_yoltage(bank, length):
    batteries = list(bank)
    pos = -1
    solution = ''
    for d in range(0, length):
        part = batteries[pos + 1:len(batteries) - length + 1 + d]
        v = max(part)
        p = part.index(v)
        solution += v
        d += 1
        pos += p + 1
    return int(solution)
