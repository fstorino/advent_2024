"""
Advent of Code 2024
Day 2
https://adventofcode.com/2024/day/2
"""
import locale
import itertools as it
import os

INPUT_FILE = os.path.join(os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))), 
    "day02_input.txt")

locale.setlocale(locale.LC_ALL, 'pt_BR')

def main() -> None:
    part1()
    part2()

def part1() -> None:
    numbers: list[str]
    count: int = 0

    with open(INPUT_FILE, newline="") as f:
        for line in f:
            numbers = line.split()
            if is_safe(numbers): count += 1
    
    print(f"\nSafe reports: {count:n}")

def part2() -> None:
    numbers: list[str]
    count: int = 0

    with open(INPUT_FILE, newline="") as f:
        for line in f:
            numbers = line.split()
            if is_safe(numbers):
                count += 1
            else:
                for new_numbers in it.combinations(numbers, len(numbers) - 1):
                    if is_safe(new_numbers):
                        count += 1
                        break
                    
    print(f"\nSafe reports (with tolerance): {count:n}")

def is_safe(numbers: list[str]) -> bool:
    curr: int
    prev: int
    diff: int
    increasing: bool
    decreasing: bool

    decreasing, increasing = True, True
    for n in range(len(numbers)):
        if not n: continue
        curr = int(numbers[n])
        prev = int(numbers[n - 1])
        diff = abs(curr - prev)
        if curr > prev and diff <= 3:
            decreasing = False
        elif curr < prev and diff <= 3:
            increasing = False
        else:
            decreasing, increasing = False, False
    
    return increasing or decreasing

if __name__ == "__main__":
    main()
