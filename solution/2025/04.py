from solution.base import Base

class Solution(Base):
    year = 2025
    day = "04"
    grid = {}

    def _parse_input(self, data):
        line_id = 0
        for line in data.splitlines():
            self.grid[line_id] = dict(enumerate(list(line)))
            line_id += 1

    def _part1(self):
        output = 0
        for line, columns in self.grid.items():
            for column, state in columns.items():
                if state == '@':
                    if self._get_neighbours(line, column) < 4:
                        output += 1
        return output

    def _part2(self):
        output = 0
        n = 1
        while n > 0:
            n = self._remove_rolls()
            output += n
        return output

    def _remove_rolls(self):
        output = 0
        for line, columns in self.grid.items():
            for column, state in columns.items():
                if state == '@':
                    if self._get_neighbours(line, column) < 4:
                        output += 1
                        self.grid[line][column] = '.'
        return output

    def _get_neighbours(self, line, column):
        n = -1
        for l in [line - 1, line, line + 1]:
            for c in [column - 1, column, column + 1]:
                try:
                    neighbour = self.grid[l][c]
                except KeyError:
                    neighbour = '-'
                if neighbour == '@':
                    n += 1
        return n
