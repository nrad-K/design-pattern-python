from abc import ABC, abstractmethod
from typing import Self


class Handler(ABC):
    @abstractmethod
    def handle(self: Self, request: int) -> bool:
        pass


class ConcreteHandler1(Handler):
    def handle(self: Self, request: int) -> bool:
        min_req = 0
        max_req = 10
        if min_req < request <= max_req:
            print(f"Request {request} handled in handler 1")
            return True
        return False


class ConcreteHandler2(Handler):
    def handle(self: Self, request: int) -> bool:
        min_req = 10
        max_req = 20
        if min_req < request <= max_req:
            print(f"Request {request} handled in handler 2")
            return True
        return False


class ConcreteHandler3(Handler):
    def handle(self: Self, request: int) -> bool:
        min_req = 30
        max_req = 40
        if min_req < request <= max_req:
            print(f"Request {request} handled in handler 3")
            return True
        return False


class DefaultHandler(Handler):
    def handle(self: Self, request: int) -> bool:
        print(f"End of chain, no handler for {request}")
        return True


class Client:
    def __init__(self: Self) -> None:
        self.handlers = [
            ConcreteHandler1(),
            ConcreteHandler2(),
            ConcreteHandler3(),
            DefaultHandler(),
        ]

    def delegate(self: Self, requests: list[int]) -> None:
        for request in requests:
            for handler in self.handlers:
                if handler.handle(request):
                    break


if __name__ == "__main__":
    client = Client()

    requests = [2, 5, 14, 22, 18, 3, 35, 27, 20]

    client.delegate(requests)
