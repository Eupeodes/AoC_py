import math
from solution.base import Base

class Solution(Base):
    year = 2025
    day = "01"
    position = 50
    at_zero = 0
    all_zeros = 0

    def parse_input(self, data):
        return data.splitlines()

    def part1(self):
        for line in self.input:
            self.dial(line)
        return self.at_zero

    def part2(self):
        return self.all_zeros

    def dial(self, action):
        steps = int(action[1:])
        self.all_zeros += math.floor(steps / 100)
        delta = (-1 if action[0] == 'L' else 1) * (steps % 100)
        next_position = self.position + delta
        if self.position > 0 and not 0 < next_position < 100:
            self.all_zeros += 1
        self.position = next_position % 100

        if self.position == 0:
            self.at_zero += 1
