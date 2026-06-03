import pytest

from src.category import Category
from src.lawngrass import LawnGrass
from src.products import Product
from src.smartphone import Smartphone


@pytest.fixture
def fix_product():
    return Product(name="QLED 4K", description="Фоновая подсветка", price=100000, quantity=101)


@pytest.fixture
def fix_product_2():
    return Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8)


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


@pytest.fixture
def grass_product_1():
    grass1 = LawnGrass("Газонная трава",
                       "Элитная трава для газона",
                       500.0,
                       20,
                       "Россия",
                       "7 дней",
                       "Зеленый")
    return grass1


@pytest.fixture
def grass_product_2():
    grass2 = LawnGrass("Газонная трава 2",
                       "Выносливая трава",
                       450.0,
                       15,
                       "США",
                       "5 дней",
                       "Темно-зеленый")


@pytest.fixture
def smartphone_product_1():
    smartphone1 = Smartphone("Samsung Galaxy S23 Ultra",
                             "256GB, Серый цвет, 200MP камера",
                             180000.0,
                             5,
                             95.5,
                             "S23 Ultra",
                             256,
                             "Серый")


@pytest.fixture
def smartphone_product_2():
    smartphone2 = Smartphone("Iphone 15",
                             "512GB, Gray space",
                             210000.0,
                             8,
                             98.2,
                             "15",
                             512,
                             "Gray space")
