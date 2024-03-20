import pathlib
import sys

print(f"{sys.path=}")

# run in pycharm
# sys.path = [
#    "/Users/andigorgoyle/PycharmProjects/pycharm_black_magic/pycharm_only",
#    "/Users/andigorgoyle/PycharmProjects/pycharm_black_magic", <- LOOK WHAT Pycharm did
#    "/Library/Frameworks/Python.framework/Versions/3.10/lib/python310.zip",
#    "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10",
#    "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/lib-dynload",
#    "/Users/andigorgoyle/PycharmProjects/pycharm_black_magic/venv/lib/python3.10/site-packages",
# ]

import helpers


def find_most_calories(file_name: str):
    return max(_get_all_elf_calories(file_name=file_name))


def _get_all_elf_calories(file_name: str) -> list[int]:
    with open(pathlib.Path(__file__).parent / file_name, "r") as puzzle_input:
        calories_per_elf = puzzle_input.read().split("\n\n")
        total_calories_per_elf = list()
        for elf in calories_per_elf:
            all_calories_strings = elf.strip().split("\n")
            total_calories_per_elf.append(sum(list(map(int, all_calories_strings))))
    return total_calories_per_elf


helpers.print_result(my_func=find_most_calories, file_name="puzzle_input.txt")
