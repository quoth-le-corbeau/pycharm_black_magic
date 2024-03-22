import time
import sys

print(f"{sys.path=}")
print(f"{sys.modules=}")


import sameLevelHelpers


def find_most_calories(file_name: str):
    return max(sameLevelHelpers.get_all_elf_calories(file_name=file_name))


start = time.perf_counter()
print(find_most_calories("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
