from abc import ABC, abstractmethod
from typing import Self


class Component(ABC):
    @abstractmethod
    def operation(self: Self) -> str:
        pass


class Leaf(Component):
    def operation(self: Self) -> str:
        return "Leaf"


class Composite(Component):
    _children: list[Component]

    def __init__(self: Self) -> None:
        self._children = []

    def add(self: Self, component: Component) -> None:
        self._children.append(component)

    def operation(self: Self) -> str:
        results: list[str] = [child.operation() for child in self._children]
        return f"Branch({'+'.join(results)})"


if __name__ == "__main__":
    leaf1 = Leaf()
    leaf2 = Leaf()

    composite = Composite()
    composite.add(leaf1)
    composite.add(leaf2)

    print(leaf1.operation())
    print(leaf2.operation())
    print(composite.operation())
