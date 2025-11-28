from abc import ABC, abstractmethod
import time

class Base(ABC):
    start = time.time()
    input = {}

    def __init__(self):
        with open(f'input/{self.year}/{self.day}.txt', 'r') as f:
            self.realinput = f.read()
        try:
            with open(f'input/{self.year}/{self.day}_example.txt', 'r') as f:
                self.testinput = f.read()
        except FileNotFoundError:
            self.testinput = ""

    def timing(self):
        end = time.time()
        print(f"Execution Time: {end - self.start} seconds")
        self.start = end

    def run(self):
        self.timing()
        if self.testinput:
            self.input = self.parse_input(self.testinput)
            print("Part 1 (test):", self.part1())
            self.timing()
            print("Part 2 (test):", self.part2())
            self.timing()

        self.input = self.parse_input(self.realinput)
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
