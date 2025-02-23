"""
Advent of Code 2024
Day 4
https://adventofcode.com/2024/day/4
"""
import locale
import os

INPUT_FILE = os.path.join(os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))), 
    "day04_input.txt")

locale.setlocale(locale.LC_ALL, 'pt_BR')

def main() -> None:
    word_search: str
    char_grid: tuple[tuple[str]]

    # lê o input e converte e grid
    with open(INPUT_FILE, newline="") as f:
        word_search = f.read()
    
    char_grid = tuple(tuple(linha) for linha in word_search.splitlines())

    part1(char_grid)
    part2(char_grid)

def part1(char_grid: tuple[tuple[str]]) -> None:
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
    count: int = 0
    y_max: int = len(char_grid)
    x_max: int = len(char_grid[0])

    print(f"\nProcurando a palavra '{word}' num grid {x_max}x{y_max}...", end="", flush=True)
    for y in range(y_max):
        for x in range(x_max):
            for direção in direções:
                grid_word = get_word(word, char_grid, x, y, direções[direção]["x_step"], direções[direção]["y_step"])
                if word == grid_word:
                    count += 1
    print("OK\n")
    print(f"Palavras '{word}' encontradas: {count:n} ({count})")
    
def get_word(word: str, char_grid: tuple[tuple[str]], x: int, y: int, x_step: int, y_step: int) -> str:
    x_stop = x + x_step * (len(word) - 1)
    y_stop = y + y_step * (len(word) - 1)
    y_max: int = len(char_grid)
    x_max: int = len(char_grid[0])
    grid_word: str = ""
    
    # retorna "" se fora dos limites do grid
    if (x_stop >= x_max) or (x_stop < 0): return ""
    if (y_stop >= y_max) or (y_stop < 0): return ""
    
    # retorna a palavra na direção desejada
    for _ in range(len(word)):
        grid_word += char_grid[y][x]
        x += x_step
        y += y_step
    return grid_word

def part2(char_grid: str) -> None:
    word: str = "MAS"
    direções: dict = {
        "diag esq":       {"x_step": 1,  "y_step": 1},  # ↘️
        "diag esq rev":   {"x_step": -1, "y_step": -1}, # ↖️
        "diag dir":       {"x_step": -1, "y_step": 1},  # ↙️
        "diag dir rev":   {"x_step": 1,  "y_step": -1}  # ↗️
        }
    count: int = 0
    y_max: int = len(char_grid)
    x_max: int = len(char_grid[0])
    matches: list[list[tuple[int, int], str, bool]] = []

    print(f"\nProcurando a palavra X-'{word}' num grid {x_max}x{y_max}...", end="", flush=True)
    for y in range(y_max):
        for x in range(x_max):
            for direção in direções:
                grid_word = get_word(word, char_grid, x, y, direções[direção]["x_step"], direções[direção]["y_step"])
                if word == grid_word:
                    matches.append([(x, y), direção, False])
    print("OK\n")

    # todo: contar os matches com x e y cruzados
    count = pair(matches)
    
    print(f"Palavras X-'{word}' encontradas: {count:n} ({count})")

def get_crossword(word: str, char_grid: tuple[tuple[str]], x: int, y: int, x_step: int, y_step: int) -> str:
    x_stop = x + x_step * (len(word) - 1)
    y_stop = y + y_step * (len(word) - 1)
    y_max: int = len(char_grid)
    x_max: int = len(char_grid[0])
    grid_word: str = ""
    
    # retorna "" se fora dos limites do grid
    if (x_stop >= x_max) or (x_stop < 0): return ""
    if (y_stop >= y_max) or (y_stop < 0): return ""
    
    # retorna a palavra na direção desejada
    for _ in range(len(word)):
        grid_word += char_grid[y][x]
        x += x_step
        y += y_step
    return grid_word

def pair(matches: list[list[tuple[int, int], str, bool]]) -> int:
    count: int = 0

    for item in matches:
        if item[2]: continue
        x, y = item[0]
        match item[1]:
            case "diag esq": # ↘️
                try:
                    linha_match = matches.index([(x, y + 2), "diag dir rev", False]) # ↗️
                    item[2] = True
                    matches[linha_match][2] = True
                except:
                    pass
                try:
                    linha_match = matches.index([(x + 2, y), "diag dir", False]) # ↙️
                    item[2] = True
                    matches[linha_match][2] = True
                except:
                    pass
            case "diag dir rev": # ↗️
                try:
                    linha_match = matches.index([(x + 2, y), "diag esq rev", False]) # ↖️
                    item[2] = True
                    matches[linha_match][2] = True
                except:
                    pass
            case "diag dir": # ↙️
                try:
                    linha_match = matches.index([(x, y + 2), "diag esq rev", False]) # ↖️
                    item[2] = True
                    matches[linha_match][2] = True
                except:
                    pass
            case _:
                continue
    
    for item in matches:
        if item[2]: count += 1

    return count // 2

if __name__ == "__main__":
    main()
