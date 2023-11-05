import time
from typing import Callable


def decorator(func: Callable[[int], int]) -> Callable[[int], int]:
    def _wrapper(args: int) -> int:
        start_time = time.perf_counter()
        print("function start")
        result = func(args)
        print(f"result: {result}")
        print("function end")
        end_time = time.perf_counter()
        print(f"実行時間 = {end_time - start_time}s")
        return func(args)

    return _wrapper


@decorator
def my_sum(limit: int) -> int:
    result: int = 0
    for i in range(limit):
        result += i

    return result


if __name__ == "__main__":
    my_sum(1000)
