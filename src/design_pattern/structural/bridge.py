from abc import ABC, abstractmethod
from typing import Self


class Implementation(ABC):
    @abstractmethod
    def operation_implementation(self: Self) -> str:
        pass


class ConcreteImplementationA(Implementation):
    def operation_implementation(self: Self) -> str:
        return "ConcreteImplementationA: Here's the result on the platform A."


class ConcreteImplementationB(Implementation):
    def operation_implementation(self: Self) -> str:
        return "ConcreteImplementationB: Here's the result on the platform B."


class Abstraction:
    def __init__(self: Self, implementation: Implementation) -> None:
        self.implementation = implementation

    def operation(self: Self) -> str:
        return (
            f"Abstraction: Base operation with:\n"
            f"{self.implementation.operation_implementation()}"
        )


class ExtendedAbstraction(Abstraction):
    def operation(self: Self) -> str:
        return (
            f"ExtendedAbstraction: Extended operation with:\n"
            f"{self.implementation.operation_implementation()}"
        )


if __name__ == "__main__":
    implementation_a = ConcreteImplementationA()
    abstraction = Abstraction(implementation_a)
    print(abstraction.operation())
    print()
    implementation_b = ConcreteImplementationB()
    abstraction = ExtendedAbstraction(implementation_b)
    print(abstraction.operation())
