import sys

print(f"{sys.path=}")
import time
import pathlib

import helpers

# run in vscode:
# sys_path = sys.path = [
#     "/Users/andigorgoyle/PycharmProjects/pycharm_black_magic/works_everywhere",
#     "/Library/Frameworks/Python.framework/Versions/3.10/lib/python310.zip",
#     "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10",
#     "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/lib-dynload",
#     "/Users/andigorgoyle/PycharmProjects/pycharm_black_magic/venv/lib/python3.10/site-packages",
# ]


def find_most_calories(file_name: str):
    return max(helpers.get_all_elf_calories(file_name=file_name))


start = time.perf_counter()
print(find_most_calories("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
