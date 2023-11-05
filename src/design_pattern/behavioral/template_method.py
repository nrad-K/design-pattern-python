from abc import ABC, abstractmethod
from typing import Self


class AbstractClass(ABC):
    def template_method(self: Self) -> None:
        self.base_operation1()
        self.required_operations1()
        self.base_operation2()
        self.hook1()
        self.required_operations2()
        self.base_operation3()
        self.hook2()

    def base_operation1(self: Self) -> None:
        print("AbstractClass says: I am doing the bulk of the work")

    def base_operation2(self: Self) -> None:
        print("AbstractClass says: But I let subclasses override some operations")

    def base_operation3(self: Self) -> None:
        print("AbstractClass says: But I am doing the bulk of the work anyway")

    @abstractmethod
    def required_operations1(self: Self) -> None:
        pass

    @abstractmethod
    def required_operations2(self: Self) -> None:
        pass

    def hook1(self: Self) -> None:  # noqa: B027
        pass

    def hook2(self: Self) -> None:  # noqa: B027
        pass


class ConcreteClass1(AbstractClass):
    def required_operations1(self: Self) -> None:
        print("ConcreteClass1 says: Implemented Operation1")

    def required_operations2(self: Self) -> None:
        print("ConcreteClass1 says: Implemented Operation2")


class ConcreteClass2(AbstractClass):
    def required_operations1(self: Self) -> None:
        print("ConcreteClass2 says: Implemented Operation1")

    def required_operations2(self: Self) -> None:
        print("ConcreteClass2 says: Implemented Operation2")

    def hook1(self: Self) -> None:
        print("ConcreteClass2 says: Overridden Hook1")


if __name__ == "__main__":
    print("Same client code can work with different subclasses:")
    concrete_class1 = ConcreteClass1()
    concrete_class1.template_method()

    print("\n")

    print("Same client code can work with different subclasses:")
    concrete_class2 = ConcreteClass2()
    concrete_class2.template_method()
