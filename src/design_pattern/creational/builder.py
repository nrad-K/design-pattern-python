from abc import ABC, abstractmethod
from typing import Self


class Builder(ABC):
    @abstractmethod
    def build_a(self: Self) -> str:
        pass

    @abstractmethod
    def build_b(self: Self) -> str:
        pass

    @abstractmethod
    def build_c(self: Self) -> str:
        pass


class Builder1(Builder):
    def build_a(self: Self) -> str:
        return "build A1"

    def build_b(self: Self) -> str:
        return "build B1"

    def build_c(self: Self) -> str:
        return "build C1"


class Builder2(Builder):
    def build_a(self: Self) -> str:
        return "build A2"

    def build_b(self: Self) -> str:
        return "build B2"

    def build_c(self: Self) -> str:
        return "build C2"


class Director:
    def __init__(self: Self, builder: Builder) -> None:
        self.build = (
            f"Build: {builder.build_a()} {builder.build_b()} {builder.build_c()}"
        )


if __name__ == "__main__":
    builder1 = Director(Builder1())
    builder2 = Director(Builder2())

    print(builder1.build)
    print(builder2.build)
