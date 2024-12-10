"""
Advent of Code 2024
Day 1
https://adventofcode.com/2024/day/1
"""
import locale
from urllib import request

locale.setlocale(locale.LC_ALL, 'pt_BR')

def main() -> None:
    list1: tuple[str]
    list2: tuple[str]

    # populate lists
    with open(R"fstorino/advent_2024/day01_input.txt", newline="") as f:
        list1, list2 = zip(*(line.split() for line in f))

    part1(list1, list2)
    part2(list1, list2)

def part1(list1: tuple[str], list2: tuple[str]) -> None:
    # calculate difference and sum
    diff: list[int] = [abs(int(val1) - int(val2)) for val1, val2 in zip(sorted(list1), sorted(list2))]
    result = sum(diff)
    
    print(f"\nSoma das diferenças: {result:n} ({result})")

def part2(list1: tuple[str], list2: tuple[str]) -> None:
    score: int = 0

    # iterate through list1 and calculate similarity score
    for number in set(list1):
        score += int(number) * list2.count(number)

    print(f"\nScore de similaridade: {score:n} ({score})")

if __name__ == "__main__":
    main()
