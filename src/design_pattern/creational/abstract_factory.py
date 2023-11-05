from abc import ABC, abstractmethod
from typing import Self


# Product
class Product(ABC):
    @abstractmethod
    def print_name(self: Self) -> None:
        pass


class ProductA(Product):
    @abstractmethod
    def print_name(self: Self) -> None:
        pass


class ProductB(Product):
    @abstractmethod
    def print_name(self: Self) -> None:
        pass


# Factory
class AbstractFactory(ABC):
    @abstractmethod
    def check_product(self: Self) -> None:
        pass

    @abstractmethod
    def create_product_a(self: Self) -> ProductA:
        pass

    @abstractmethod
    def create_product_b(self: Self) -> ProductB:
        pass


class ProductFactory1(AbstractFactory):
    def check_product(self: Self) -> None:
        self.create_product_a().print_name()
        self.create_product_b().print_name()

    @classmethod
    def create_product_a(cls: type[Self]) -> ProductA:
        return cls.ProductA1()

    @classmethod
    def create_product_b(cls: type[Self]) -> ProductB:
        return cls.ProductB1()

    class ProductA1(ProductA):
        def print_name(self: Self) -> None:
            print("Product A1")

    class ProductB1(ProductB):
        def print_name(self: Self) -> None:
            print("Product B1")


class ProductFactory2(AbstractFactory):
    def check_product(self: Self) -> None:
        self.create_product_a().print_name()
        self.create_product_b().print_name()

    @classmethod
    def create_product_a(cls: type[Self]) -> ProductA:
        return cls.ProductA2()

    @classmethod
    def create_product_b(cls: type[Self]) -> ProductB:
        return cls.ProductB2()

    class ProductA2(ProductA):
        def print_name(self: Self) -> None:
            print("Product A2")

    class ProductB2(ProductB):
        def print_name(self: Self) -> None:
            print("Product B2")


if __name__ == "__main__":
    factory1 = ProductFactory1()
    factory2 = ProductFactory2()
    factory1.check_product()
    print("--------------------------------")
    factory2.check_product()
