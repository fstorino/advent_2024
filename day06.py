"""
Advent of Code 2024
Day 6
https://adventofcode.com/2024/day/6
"""
import locale
import os
import itertools as it
from math import log10, floor

INPUT_FILE = os.path.join(os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))), 
    "day06_input.txt")

locale.setlocale(locale.LC_ALL, "pt_BR")

def main() -> None:
    result_part1: int
    result_part2: int
    
    # Lê o input e cria o mapa
    with open(INPUT_FILE) as f:
        map = Map(f.read().splitlines())
    
    result_part1 = part1(map)
    print(f"Distinct positions visited: {BOLD}{GREEN}{result_part1:n}{RESET} ({result_part1})\n")

    #result_part2 = part2(updates, rules)
    #print(f"Soma incorretos: {BOLD}{GREEN}{result_part2:n}{RESET} ({result_part2})")   

    return

class Map():
    def __init__(self, input: list[str]) -> None:
        """
        Create a Map object
        """
        self.map = [list(_) for _ in input]
        # initialize variables
        self.x: int; self.y: int
        self.guard_pos: tuple[int, int]
        self.__movements = {
        "<": {"x_step": -1,
              "y_step": 0,
              "direction": "esquerda"},
        "^": {"x_step": 0,
              "y_step": -1,
              "direction": "cima"},
        ">": {"x_step": 1,
              "y_step": 0,
              "direction": "direita"},
        "v": {"x_step": 0,
              "y_step": 1,
              "direction": "baixo"}}
        self.__directions = list(self.__movements.keys())
        # set properties
        self.width: int = len(self.map[0])
        self.height: int = len(self.map)
        self.x, self.y = self.guard_pos = self.find_guard()
        self.cursor: str = ""
        self.update_movement()

    def update_movement(self):
        """
        Update the guard movement variables
        """
        # inicializa as variáveis de cursor
        if not self.cursor:
            self.cursor = self.map[self.y][self.x]
            self.__cursor = it.islice(it.cycle(self.__directions), 
                                      self.__directions.index(self.cursor),
                                      None)
            next(self.__cursor)
        # atualiza as variáveis de direção e movimento
        self.direction: str = self.__movements[self.cursor]["direction"]
        self.__x_step: int = self.__movements[self.cursor]["x_step"]
        self.__y_step: int = self.__movements[self.cursor]["y_step"]

    def print(self):
        """
        Print the map
        """
        x_offset: int = floor(log10(self.height)) + 1

        def x_header() -> list[str]:
            """
            Return the horizontal headers
            """
            # orders of magnitude
            orders = floor(log10(self.width)) + 1
            lines: list[str] = [list() for _ in range(orders)]
            
            for number in range(self.width):
                text = str(number).rjust(orders)
                for order in range(orders):
                    lines[order] += text[order]

            for idx, line in enumerate(lines):
                lines[idx] = "".join(line)

            return lines

        def y_header() -> list[str]:
            """
            Return the vertical headers
            """
            nonlocal x_offset
            # orders of magnitude
            orders = x_offset
            lines: list[str] = [str(number).rjust(orders) 
                                for number in range(self.height)]
            
            return lines

        def color(text: str) -> str:
            colored_text = ""
            for char in text:
                match char:
                    case "#":
                        color = f"{RED}"
                    case _ if char in self.__directions:
                        color = f"{GREEN}"
                    case _:
                        color = ""
                colored_text += f"{color}{char}{RESET}"
            return colored_text

        # print x_header
        for header in x_header():
            print(f"{" " * x_offset}{YELLOW}{header}{RESET}")
        # print y_header + map
        for header, line in zip(y_header(), self.map):
            print(f"{YELLOW}{header}{RESET}{color(line)}")

    def find_guard(self) -> tuple[int, int]:
        """
        Find the guard and return their (x, y) position
        """
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] in self.__directions:
                    return (x, y)

    def move_guard(self) -> bool:
        """
        Move guard. Returns False when there are no more valid moves
        """
        next_x: int = self.x + self.__x_step
        next_y: int = self.y + self.__y_step
        # Check boundaries
        if (next_x < 0 or next_x >= self.width) or \
           (next_y < 0 or next_y >= self.height):
            self.map[self.y][self.x] = "X"
            return False
        # Check next character
        next_char = self.map[next_y][next_x]
        if next_char == "#": # gira o guarda
            self.spin_guard()
        else: # move o guarda
            self.map[self.y][self.x] = "X"
            self.x, self.y = self.guard_pos = next_x, next_y
        # Redesenha o cursor
        self.map[self.y][self.x] = self.cursor
        return True

    def spin_guard(self) -> None:
        self.cursor = next(self.__cursor)
        self.update_movement()

    def count_visited(self) -> int:
        """
        Count the visited squares
        """
        return sum([line.count("X") for line in self.map])

def clear_screen() -> None:
    if os.name == "nt": # Windows
        os.system("cls")
    else: # Linux, MacOS
        os.system("clear")
    return

def part1(map: Map) -> int:
    result: int = 0

    # Move guard until no more moves available
    while map.move_guard():
        pass
    # Count visited squares
    result = sum([line.count("X") for line in map.map])
    
    return result

def part2(map: Map) -> int:
    result: int = 0

    return result

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
