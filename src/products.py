from src.baseproduct import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        if quantity > 0:
            self.name = name
            self.description = description
            self.__price = price
            self.quantity = quantity
            super().__init__()
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is type(self):
            self_result = self.price * self.quantity
            other_result = other.price * other.quantity
            return self_result + other_result
        else:
            raise TypeError("Невозможно сложить товары разных классов")

    @classmethod
    def new_product(cls, my_dict):
        name = my_dict.get("name")
        description = my_dict.get("description")
        price = my_dict.get("price")
        quantity = my_dict.get("quantity")
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price
