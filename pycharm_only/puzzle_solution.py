import sys

print(f"{sys.path=}")

# run in pycharm
# sys.path = [
#     "/home/lecorbeau/CodeProjects/pycharm_black_magic/pycharm_only",
#     "/home/lecorbeau/CodeProjects/pycharm_black_magic",  # LOOK WHAT PyCharm did!
#     "/usr/lib/python311.zip",
#     "/usr/lib/python3.11",
#     "/usr/lib/python3.11/lib-dynload",
#     "/home/lecorbeau/CodeProjects/pycharm_black_magic/venv/lib/python3.11/site-packages",
# ]


import pathlib
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
