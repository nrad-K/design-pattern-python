from copy import deepcopy
from typing import Final, Self


class Prototype:
    x: int
    y: Final[int]

    def __init__(self: Self, x: int, y: int) -> None:
        self.x = x
        self.y = y


if __name__ == "__main__":
    proto1 = Prototype(2, 3)
    proto2 = deepcopy(proto1)
    proto2.x = 10
    print(proto1.x, proto1.y)
    print(proto2.x, proto2.y)
