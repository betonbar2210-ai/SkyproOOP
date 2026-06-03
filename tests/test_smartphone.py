import pytest


def test_init_smartphone(smartphone_product_1):
    assert smartphone_product_1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone_product_1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone_product_1.price == 180000.0
    assert smartphone_product_1.quantity == 2
    assert smartphone_product_1.efficiency == 95.5
    assert smartphone_product_1.model == "S23 Ultra"
    assert smartphone_product_1.memory == 256
    assert smartphone_product_1.color == "Серый"


def test_add_smartphone(smartphone_product_1, smartphone_product_2):
    assert smartphone_product_1 + smartphone_product_2 == 570000.0


def test_add_smartphone_error(smartphone_product_1, grass_product_1):
    with pytest.raises(TypeError):
        smartphone_product_1 + grass_product_1
