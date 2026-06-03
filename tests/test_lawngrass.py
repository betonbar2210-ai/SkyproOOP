import pytest


def test_init_lawngrass(grass_product_1):
    assert grass_product_1.name == "Газонная трава"
    assert grass_product_1.description == "Элитная трава для газона"
    assert grass_product_1.price == 500.0
    assert grass_product_1.quantity == 2
    assert grass_product_1.country == "Россия"
    assert grass_product_1.germination_period == "7 дней"
    assert grass_product_1.color == "Зеленый"


def test_add_lawngrass(grass_product_1, grass_product_2):
    assert grass_product_1 + grass_product_2 == 1450.0


def test_add_lawngrass_error(grass_product_1, smartphone_product_1):
    with pytest.raises(TypeError):
        grass_product_1 + smartphone_product_1
