from src.category import Category
from tests.conftest import fix_product


def test_category_init(fix_category_1, fix_category_2):
    assert fix_category_1.name == 'Смартфоны'
    assert fix_category_1.description == 'Смартфоны, как средство'

    assert fix_category_2.name == 'Телевизоры'
    assert fix_category_2.description == 'Современный телевизор'

    assert fix_category_1.category_count == 2
    assert fix_category_2.category_count == 2
    assert fix_category_1.product_count == 2
    assert fix_category_2.product_count == 2


def test_products_property(fix_category_1):
    assert fix_category_1.products == "QLED 4K, 100000 руб. 101: шт.\n"


def test_add_product(fix_category_1, fix_product):
    assert len(fix_category_1.products_list) == 1
    fix_category_1.add_product(fix_product)
    assert len(fix_category_1.products_list) == 2

