from typing import ClassVar, Self


class Flyweight:
    _FlyweightPool: ClassVar[dict[str, Self]] = {}
    state: str
    obj_id: int

    def __new__(cls: type[Self], state: str) -> Self:
        obj = cls._FlyweightPool.get(state, None)
        if obj is None or not isinstance(obj, cls):
            obj = object.__new__(cls)
            cls._FlyweightPool[state] = obj
            obj.state = state
            obj.obj_id = id(obj)
        return obj

    def operation(self: Self) -> None:
        print(f"Intrinsic State: {self.state}  ID: {self.obj_id}")


if __name__ == "__main__":
    flyweight1 = Flyweight("state1")
    flyweight2 = Flyweight("state1")  # This will return the same instance as flyweight1
    flyweight3 = Flyweight("state2")

    flyweight1.operation()
    flyweight2.operation()
    flyweight3.operation()
