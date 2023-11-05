from abc import ABC, abstractmethod
from typing import Self


class Subject(ABC):
    @abstractmethod
    def request(self: Self) -> str:
        pass


class RealSubject(Subject):
    def request(self: Self) -> str:
        return "RealSubject: Handling request."


class Proxy(Subject):
    def __init__(self: Self) -> None:
        self.__real_object = RealSubject()

    def request(self: Self) -> str:
        return (
            "Proxy: Delegating request to RealSubject.\n" + self.__real_object.request()
        )


if __name__ == "__main__":
    proxy = Proxy()
    print(proxy.request())
