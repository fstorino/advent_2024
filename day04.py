"""
Advent of Code 2024
Day 4
https://adventofcode.com/2024/day/4
"""
import locale
import re

INPUT_FILE = R"C:\Users\fstorino\Downloads\day04_input.txt"

locale.setlocale(locale.LC_ALL, 'pt_BR')

def main() -> None:
    part1()
    part2()

def part1() -> None:
    word_search: str = """
....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX
        """.strip()
    word: str = "XMAS"
    word_pos: int = 0
    x_pos: int = 0
    y_pos: int = 0
    direções: dict = \
        {"horizontal":
            {"x_start": 0,
            "x_skip": 1,
            "y_start": 0,
            "y_skip": 0},
        "horizontal_reverso":
            {"x_start": 1,
            "x_skip": -1,
            "y_start": 0,
            "y_skip": 0},
        "vertical":
            {"x_start": 0,
            "x_skip": 0,
            "y_start": 0,
            "y_skip": 1},
        "vertical_reverso":
            {"x_start": 0,
            "x_skip": 0,
            "y_start": 1,
            "y_skip": -1},
        "diag_esq":
            {"x_start": 0,
            "x_skip": 1,
            "y_start": 0,
            "y_skip": 1},
        "diag_esq_reverso":
            {"x_start": 1,
            "x_skip": -1,
            "y_start": 1,
            "y_skip": -1},
        "diag_dir":
            {"x_start": 1,
            "x_skip": -1,
            "y_start": 0,
            "y_skip": 1},
        "diag_dir_reverso":
            {"x_start": 0,
            "x_skip": 1,
            "y_start": 1,
            "y_skip": -1}
        }
    
    linhas = word_search.splitlines()
    y_max = len(linhas)
    x_max = len(linhas[0])
    for direção in direções:
        print(f"{direção = }")
        for lin in range(direções[direção]["x_start"] * x_max):
            for col in range(x_max):
                if linhas[lin][col]:
                    ...
    


def part2() -> None:
    ...

if __name__ == "__main__":
    main()
