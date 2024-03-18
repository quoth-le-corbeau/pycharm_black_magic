import time
import pathlib


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


start = time.perf_counter()
print(find_most_calories("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
