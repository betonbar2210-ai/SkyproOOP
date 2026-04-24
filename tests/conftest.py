import pytest

from src.category import Category
from src.products import Product


@pytest.fixture
def fix_product():
    return Product(name="QLED 4K", description="Фоновая подсветка", price=100000, quantity=101)


@pytest.fixture
def fix_category_1():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство",
        products=[Product(name="QLED 4K", description="Фоновая подсветка", price=100000, quantity=101)],
    )


@pytest.fixture
def fix_category_2():
    return Category(
        name="Телевизоры",
        description="Современный телевизор",
        products=[Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)],
    )


@pytest.fixture
def utils_json():
    return [
        {
            "name": "Смартфоны",
            "description":
                "Смартфоны, как средство не только коммуникации",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
                {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
            ],
        },
        {
            "name": "Телевизоры",
            "description": "Современный телевизор",
            "products": [
                {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
            ],
        },
    ]
