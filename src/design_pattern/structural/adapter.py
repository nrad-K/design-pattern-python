from abc import ABC, abstractmethod
from typing import Final, Self


class Target(ABC):
    @abstractmethod
    def request(self: Self) -> str:
        return "Target: The default target's behavior."


class Adaptee:
    def specific_request(self: Self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target, Adaptee):
    def request(self: Self) -> str:
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"


class IAdapter(Target):
    adaptee: Final[Adaptee]

    def __init__(self: Self, cls: type[Adaptee]) -> None:
        self.adaptee = cls()

    def request(self: Self) -> str:
        return f"Adapter: (TRANSLATED) {self.adaptee.specific_request()[::-1]}"


if __name__ == "__main__":
    adapter = Adapter()
    print(adapter.request())

    iadapter = IAdapter(Adaptee)
    print(iadapter.request())
