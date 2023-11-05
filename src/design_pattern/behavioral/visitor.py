from abc import ABC, abstractmethod
from typing import Self


class Visitor(ABC):
    @abstractmethod
    def visit(self: Self, element: str) -> None:
        pass


class ConcreteVisitor1(Visitor):
    def visit(self: Self, element: str) -> None:
        print(f"ConcreteVisitor1 visited {element}")


class ConcreteVisitor2(Visitor):
    def visit(self: Self, element: str) -> None:
        print(f"ConcreteVisitor2 visited {element}")


class Element:
    def accept(self: Self, visitor: Visitor) -> None:
        element = str(self)
        visitor.visit(element)


if __name__ == "__main__":
    element = Element()
    visitor1 = ConcreteVisitor1()
    visitor2 = ConcreteVisitor2()

    element.accept(visitor1)
    element.accept(visitor2)
