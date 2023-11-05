from typing import Self


class Memento:
    _state: str

    def __init__(self: Self, state: str) -> None:
        self._state = state

    def get_saved_state(self: Self) -> str:
        return self._state


class Originator:
    _state = ""

    def set_state(self: Self, state: str) -> None:
        print(f"Originator: Setting state to {state}")
        self._state = state

    def save_to_memento(self: Self) -> Memento:
        print("Originator: Saving to Memento.")
        return Memento(self._state)

    def restore_from_memento(self: Self, memento: Memento) -> None:
        self._state = memento.get_saved_state()
        print(f"Originator: State after restoring from Memento: {self._state}")


saved_states = []
originator = Originator()

originator.set_state("State1")
originator.set_state("State2")
saved_states.append(originator.save_to_memento())

originator.set_state("State3")
saved_states.append(originator.save_to_memento())

originator.set_state("State4")

originator.restore_from_memento(saved_states[0])
