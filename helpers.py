import time
from typing import Callable


def print_result(my_func: Callable, file_name: str) -> None:
    start = time.perf_counter()
    print(my_func(file_name))
    print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
