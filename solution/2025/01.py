import math
from solution.base import Base

class Solution(Base):
    year = 2025
    day = "01"
    position = 50
    positions = {0: 0}
    through = 0
    
    def parse_input(self, data):
        return data.splitlines()

    def part1(self):
        for line in self.input:
            self.dial(line)
        return self.positions[0]

    def part2(self):
        return self.positions[0] + self.through

    def dial(self, action):
        dir = action[0]
        amount = int(action[1:])
        if dir == 'R':
            next = self.position + amount
            through = math.floor((next - 1) / 100)
        elif dir == 'L':
            next = self.position - amount
            if next < 0:
                through = math.floor((100 - next) / 100)
                if self.position == 0 or next % 100 == 0:
                    through -= 1
            else:
                through = 0
        self.through += through
        self.position = next % 100
        if self.position not in self.positions:
            self.positions[self.position] = 1
        else:
            self.positions[self.position] += 1
