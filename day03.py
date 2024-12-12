"""
Advent of Code 2024
Day 3
https://adventofcode.com/2024/day/3
"""
import locale
import re
import os

INPUT_FILE = os.path.join(os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))), 
    "day03_input.txt")

locale.setlocale(locale.LC_ALL, 'pt_BR')

def main() -> None:
    part1()
    part2()

def part1() -> None:
    x: int; y: int
    result: int = 0
    pattern: str = r"mul\((\d{1,3}),(\d{1,3})\)"

    with open(INPUT_FILE, newline="") as f:
        string = f.read()

    for operation in re.finditer(pattern, string):
        x, y = (int(_) for _ in operation.groups())
        result += x * y
    
    print(f"\nSum: {result:n} ({result})")

def part2() -> None:
    x: int; y: int
    result: int = 0
    pattern: str = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"
    ignore_next: bool = False

    with open(INPUT_FILE, newline="") as f:
        string = f.read()
        for operation in re.finditer(pattern, string):
            if operation.group() == "don't()":
                ignore_next = True
                continue
            if operation.group() == "do()":
                ignore_next = False
                continue
            if ignore_next:
                continue
            
            x, y = (int(_) for _ in operation.groups())
            result += x * y
    
    print(f"\nSum do(): {result:n} ({result})")

if __name__ == "__main__":
    main()
