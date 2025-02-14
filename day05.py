"""
Advent of Code 2024
Day 5
https://adventofcode.com/2024/day/5
"""
import locale
import os
import itertools as it

INPUT_FILE = os.path.join(os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))), 
    "day05_input.txt")

locale.setlocale(locale.LC_ALL, 'pt_BR')

def main() -> None:
    rules: list[list[int, int]] = []
    updates: list[list[int]] = []
    result_part1: int
    result_part2: int
    
    # lê o input e gera a lista de regras (rules) e a lista de atualizações (updates)
    with open(INPUT_FILE) as f:
        for line in f.readlines():
            line = line.strip()
            if "|" in line:
                rules.append(list(map(int, line.split("|"))))
            elif line:
                updates.append(list(map(int, line.split(","))))
    
    print()
    print(f"Regras:  {YELLOW}{len(rules):n}{RESET}")
    print(f"Updates: {YELLOW}{len(updates):n}{RESET}\n")
    
    result_part1 = part1(updates, rules)
    print(f"Soma corretos: {BOLD}{GREEN}{result_part1:n}{RESET} ({result_part1})\n")
    
    result_part2 = part2(updates, rules)
    print(f"Soma incorretos: {BOLD}{GREEN}{result_part2:n}{RESET} ({result_part2})")   

def part1(updates: list[list[int]], rules: list[list[int, int]]) -> int:
    result: int = 0

    for update in updates:
        # Se estiver na ordem correta, adiciona o valor do meio à soma
        if correctly_ordered_update(update, rules):
            mid_value = update[(len(update) - 1) // 2]
            result += mid_value
    
    return result

def part2(updates: list[list[int]], rules: list[list[int, int]]) -> None:
    result: int = 0

    for update in updates:
        # Se estiver na ordem incorreta, corrige e adiciona o valor do meio à soma
        if correctly_ordered_update(update, rules):
            continue
        else:
            correct_update_order(update, rules)
            mid_value = update[(len(update) - 1) // 2]
            result += mid_value
    
    return result

def correctly_ordered_update(update: list[int], rules: list[list[int, int]]) -> bool:
    for prev_page in range(len(update)):
        for next_page in range(prev_page + 1, len(update)):
            if ([update[next_page], update[prev_page]] in rules):
                return False

    return True

def correct_update_order(update: list[int], rules: list[list[int, int]]) -> tuple[int]:
    while not correctly_ordered_update(update, rules):
        for prev_page in range(len(update)):
            for next_page in range(prev_page + 1, len(update)):
                if ([update[next_page], update[prev_page]] in rules):
                    # if incorrect order, swap values
                    update[next_page], update[prev_page] = update[prev_page], update[next_page]

# ANSI escape codes
RESET = "\033[0m"

# ANSI escape codes for text colors
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# ANSI escape codes for text styles
BOLD = "\033[1m" + GREEN
ITALIC = "\033[3m" + YELLOW
BOLD_ITALIC = BOLD + ITALIC + CYAN
SUPERSCRIPT = MAGENTA

if __name__ == "__main__":
    main()
