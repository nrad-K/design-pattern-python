from abc import ABC, abstractmethod
from typing import Optional, Self


class Mediator(ABC):
    @abstractmethod
    def notify(self: Self, sender: object, event: str) -> None:
        pass


class BaseComponent:
    _mediator: Optional[Mediator]

    def __init__(self: Self, mediator: Optional[Mediator] = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self: Self) -> Optional[Mediator]:
        return self._mediator

    @mediator.setter
    def mediator(self: Self, mediator: Optional[Mediator] = None) -> None:
        self._mediator = mediator


class Component1(BaseComponent):
    def do_a(self: Self) -> None:
        print("Component 1 does A.")
        if self.mediator is not None:
            self.mediator.notify(self, "A")

    def do_b(self: Self) -> None:
        print("Component 1 does B.")
        if self.mediator is not None:
            self.mediator.notify(self, "B")


class Component2(BaseComponent):
    def do_c(self: Self) -> None:
        print("Component 2 does C.")
        if self.mediator is not None:
            self.mediator.notify(self, "C")

    def do_d(self: Self) -> None:
        print("Component 2 does D.")
        if self.mediator is not None:
            self.mediator.notify(self, "D")


class ConcreteMediator(Mediator):
    def __init__(self: Self, component1: Component1, component2: Component2) -> None:
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self: Self, _: object, event: str) -> None:
        if event == "A":
            print("Mediator reacts on A and triggers following operations:")
            self._component2.do_c()
        elif event == "D":
            print("Mediator reacts on D and triggers following operations:")
            self._component1.do_b()
            self._component2.do_c()


if __name__ == "__main__":
    c1 = Component1()
    c2 = Component2()
    mediator = ConcreteMediator(c1, c2)

    c1.do_a()

    c2.do_d()
