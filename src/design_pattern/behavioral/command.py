from abc import ABC, abstractmethod
from typing import Final, Self


class Command(ABC):
    @abstractmethod
    def execute(self: Self) -> None:
        pass


class Receiver:
    def action1(self: Self) -> None:
        print("Receiver Action 1")

    def action2(self: Self) -> None:
        print("Receiver Action 2")


class ConcreteCommand1(Command):
    _receiver: Final[Receiver]

    def __init__(self: Self, receiver: Receiver) -> None:
        self._receiver = receiver

    def execute(self: Self) -> None:
        self._receiver.action1()


class ConcreteCommand2(Command):
    _receiver: Final[Receiver]

    def __init__(self: Self, receiver: Receiver) -> None:
        self._receiver = receiver

    def execute(self: Self) -> None:
        self._receiver.action2()


class Invoker:
    def __init__(self: Self) -> None:
        self._commands: list[Command] = []

    def store_command(self: Self, command: Command) -> None:
        self._commands.append(command)

    def execute_commands(self: Self) -> None:
        for command in self._commands:
            command.execute()


if __name__ == "__main__":
    # Receiver
    receiver = Receiver()

    # concrete commands
    concrete_command1 = ConcreteCommand1(receiver)
    concrete_command2 = ConcreteCommand2(receiver)

    # invoker
    invoker = Invoker()
    invoker.store_command(concrete_command1)
    invoker.store_command(concrete_command2)
    invoker.execute_commands()
