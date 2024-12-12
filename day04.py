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
    direções: dict = {
        "horizontal":         {"x_step": 1,  "y_step": 0},
        "horizontal_reverso": {"x_step": -1, "y_step": 0},
        "vertical":           {"x_step": 0,  "y_step": 1},
        "vertical_reverso":   {"x_step": 0,  "y_step": -1},
        "diag_esq":           {"x_step": 1,  "y_step": 1},
        "diag_esq_reverso":   {"x_step": -1, "y_step": -1},
        "diag_dir":           {"x_step": -1, "y_step": 1},
        "diag_dir_reverso":   {"x_step": 1,  "y_step": -1}
        }
    
    char_grid: tuple[tuple[str]] = tuple(tuple(linha) for linha in word_search.splitlines())
    y_max: int = len(char_grid)
    x_max: int = len(char_grid[0])
    for y in range(y_max):
        for x in range(x_max):
            for direção in direções:
                if word == get_word(word, char_grid, x, y, direção["x_step"], direção["y_step"]):
                    print(f"'{word}' encontrado na posição ({x},{y}) {direção}")
    
def get_word(word: str, char_grid: tuple[tuple[str]], x: int, y: int, x_step: int, y_step: int) -> str:
    x_length = (x + len(word) - 1) * x_step
    y_length = (y + len(word) - 1) * y_step
    y_max: int = len(char_grid)
    x_max: int = len(char_grid[0])
    grid_word: str = ""
    
    if x_length > x_max: return ""
    if y_length > y_max: return ""
    
    # fazer os skips corretos com base em x_skip e y_skip
    for lin in range(y, y_length, y_step):
        for col in range(x, x_length, x_step):
            grid_word += char_grid[lin][col]
    return grid_word

def part2() -> None:
    ...

if __name__ == "__main__":
    main()
