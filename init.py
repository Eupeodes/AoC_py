import os
import requests
from dotenv import load_dotenv

load_dotenv()

class Init:
    def __init__(self, year: int, day: int):
        self.session = os.getenv("AOC_SESSION")
        if self.session is None:
            raise ValueError("AOC_SESSION ontbreekt in .env")
        self.year = year
        self.day = day

        self.create_solution()
        self.fetch_input()

    def create_solution(self):
        template = f'''from days.base import Base

class Solution(Base):
    year = {self.year}
    day = "{self.day:02}"

    def part1(self):
        return

    def part2(self):
        return
'''

        with open(f'solution/{self.year}/{self.day:02}.py', 'w') as f:
            f.write(template)

    def fetch_input(self):
        url = f"https://adventofcode.com/{self.year}/day/{self.day}/input"
        cookies = {"session": self.session}

        r = requests.get(url, cookies=cookies)
        r.raise_for_status()
        
        with open(f"input/{self.year}/{self.day:02}.txt", "w") as f:
            f.write(r.text)
