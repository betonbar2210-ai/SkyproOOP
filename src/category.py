from src.products import Product


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        count = 0
        for quanti in self.__products:
            count += quanti.quantity
        return f"{self.name}, количество продуктов: {count} шт."

    @property
    def products_list(self):
        return self.__products

    @property
    def products(self):
        product_str = ""
        for prod in self.__products:
            product_str += f"{str(prod)}\n"
        return product_str

    def add_product(self, new_product):
        if isinstance(new_product, Product):
            self.__products.append(new_product)
            Category.product_count += 1
        else:
            raise TypeError("Невозможно добавить не продукт")
