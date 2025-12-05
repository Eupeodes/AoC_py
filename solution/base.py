from abc import ABC, abstractmethod
import time


class Base(ABC):  # pylint: disable=R0903
    '''Base class for AoC solution'''
    start = time.time()
    input = {}
    year = ''
    day = ''

    def __init__(self, input_suffix):
        if input_suffix:
            file = f'input/{self.year}/{self.day}_{input_suffix}.txt'
        else:
            file = f'input/{self.year}/{self.day}.txt'
        with open(file, 'r', encoding="utf-8") as f:
            self.input = self._parse_input(f.read())

    def _timing(self):
        end = time.time()
        print(f"Execution Time: {end - self.start} seconds")
        self.start = end

    def run(self):
        '''The main function'''
        self._timing()

        print("Part 1:", self._part1())
        self._timing()

        print("Part 2:", self._part2())
        self._timing()

    @abstractmethod
    def _parse_input(self, data):
        return data

    @abstractmethod
    def _part1(self):
        pass

    @abstractmethod
    def _part2(self):
        pass
