from abc import ABC, abstractmethod
import time

class Base(ABC):
    start = time.time()
    input = {}

    def __init__(self, input_suffix):
        if input_suffix:
            file = f'input/{self.year}/{self.day}_{input_suffix}.txt'
        else:
            file = f'input/{self.year}/{self.day}.txt'
        with open(file, 'r') as f:
            self.input = f.read()

    def timing(self):
        end = time.time()
        print(f"Execution Time: {end - self.start} seconds")
        self.start = end

    def run(self):
        self.input = self.parse_input(self.input)
        self.timing()

        print("Part 1:", self.part1())
        self.timing()

        print("Part 2:", self.part2())
        self.timing()

    @abstractmethod
    def parse_input(self, data):
        return data
    
    @abstractmethod
    def part1():
        pass

    
    def part2():
        pass
