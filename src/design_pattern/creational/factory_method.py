from abc import ABC, abstractmethod
from typing import Self


# Product
class Animal(ABC):
    @abstractmethod
    def print_name(self: Self) -> None:
        pass


class Cow(Animal):
    def print_name(self: Self) -> None:
        print("Cow")


class Chicken(Animal):
    def print_name(self: Self) -> None:
        print("Chicken")


# Creator
class Factory:
    def __init__(self: Self, cls: type[Animal]) -> None:
        self.animal = cls()

    def print_animal_name(self: Self) -> None:
        self.animal.print_name()


if __name__ == "__main__":
    cow = Factory(Cow)
    chicken = Factory(Chicken)
    cow.print_animal_name()
    chicken.print_animal_name()
