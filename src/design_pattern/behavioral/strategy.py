from abc import ABC, abstractmethod
from typing import Self


class Strategy(ABC):
    @abstractmethod
    def algorithm(self: Self) -> str:
        pass


class ConcreteStrategyA(Strategy):
    def algorithm(self: Self) -> str:
        return "Concrete Strategy A"


class ConcreteStrategyB(Strategy):
    def algorithm(self: Self) -> str:
        return "Concrete Strategy B"


class Context:
    def __init__(self: Self, strategy: Strategy) -> None:
        self._strategy = strategy

    def context_interface(self: Self) -> str:
        return self._strategy.algorithm()


if __name__ == "__main__":
    strategy_a = ConcreteStrategyA()
    context = Context(strategy_a)
    print(context.context_interface())

    strategy_b = ConcreteStrategyB()
    context = Context(strategy_b)
    print(context.context_interface())
