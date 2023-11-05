from typing import ClassVar, Optional, Self


class Singleton:
    instance: ClassVar[Optional[Self]] = None

    def __new__(cls: type[Self]) -> Self:
        if not isinstance(cls.instance, cls):
            cls.instance = super().__new__(cls)
        return cls.instance


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()
    print(s1 is s2)
