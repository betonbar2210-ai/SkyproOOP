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
