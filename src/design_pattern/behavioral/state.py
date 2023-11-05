from abc import ABC, abstractmethod
from typing import Self


class State(ABC):
    @abstractmethod
    def handle(self: Self) -> str:
        pass


class ConcreteStateA(State):
    def handle(self: Self) -> str:
        return "Concrete State A"


class ConcreteStateB(State):
    def handle(self: Self) -> str:
        return "Concrete State B"


class Context:
    def __init__(self: Self, state: State) -> None:
        self._state = state

    def request(self: Self) -> str:
        return self._state.handle()


if __name__ == "__main__":
    state_a = ConcreteStateA()
    context = Context(state_a)
    print(context.request())

    state_b = ConcreteStateB()
    context = Context(state_b)
    print(context.request())
