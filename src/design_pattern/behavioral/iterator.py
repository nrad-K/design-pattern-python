from typing import Self


class Iterator:
    def __init__(self: Self, *numbers: int) -> None:
        self._numbers = numbers
        self._i = 0

    def __iter__(self: Self) -> Self:
        return self

    def __next__(self: Self) -> int:
        if self._i == len(self._numbers):
            raise StopIteration
        value = self._numbers[self._i]
        self._i += 1
        return value


if __name__ == "__main__":
    my_iterator = Iterator(10, 20, 30)
    for num in my_iterator:
        print(num)
