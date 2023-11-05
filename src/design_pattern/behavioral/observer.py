from abc import ABC, abstractmethod
from typing import Self


class Observer(ABC):
    @abstractmethod
    def update(self: Self, message: str) -> None:
        pass


class Observable:
    observers: list[Observer]

    def __init__(self: Self) -> None:
        self.observers = []

    def register(self: Self, observer: Observer) -> None:
        self.observers.append(observer)

    def notify_observers(self: Self, message: str) -> None:
        for observer in self.observers:
            observer.update(message)


class ConcreteObserverA(Observer):
    def update(self: Self, message: str) -> None:
        print(f"Concrete Observer A: {message}")


class ConcreteObserverB(Observer):
    def update(self: Self, message: str) -> None:
        print(f"Concrete Observer B: {message}")


if __name__ == "__main__":
    observable = Observable()

    observer_a = ConcreteObserverA()
    observable.register(observer_a)

    observer_b = ConcreteObserverB()
    observable.register(observer_b)

    observable.notify_observers("Hello World!")
