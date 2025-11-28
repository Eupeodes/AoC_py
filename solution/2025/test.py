import numpy as np

from solution.base import Base

class Solution(Base):
    year = 2025
    day = 'test'

    def parse_input(self, data):
        return data.split(' ')

    def part1(self):
        return self.run_script()

    def part2(self):
        return self.run_script(2025)

    def run_script(self, multiplier=1):
        data = np.array([int(self.input[i]) * multiplier for i in range(len(self.input))])

        step = 0
        pos = 0
        hand = 0
        houses = len(data)

        while True:
            hand = data[pos]
            data[pos] = 0
            if hand == 0:
                return step
            pos += 1
            step += 1
            step += hand
            if hand > houses:
                t = hand // houses
                hand = hand % houses
                data += t
            if hand > 0:
                if hand > houses - pos:
                    n = houses - pos
                    hand -= n
                    data[pos:] += 1
                    pos = 0
                    data[:hand] += 1
                    pos = hand
                else:
                    data[pos:pos + hand] += 1
                    pos += hand
                    hand = 0
            if pos >= houses:
                pos = 0
