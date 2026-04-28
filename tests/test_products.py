from pyexpat.errors import messages

from src.products import Product

def test_products_init(fix_product):
    assert fix_product.name == "QLED 4K"
    assert fix_product.description == "Фоновая подсветка"
    assert fix_product.price == 100000
    assert fix_product.quantity == 101


def test_new_product():
    new_product = Product.new_product({"name": "Samsung Galaxy S23 Ultra",
         "description": "256GB, Серый цвет, 200MP камера",
         "price": 180000.0,
         "quantity": 5})
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180000.0
    assert new_product.quantity == 5

def test_price_update(capsys, fix_product):
    fix_product.price = 0
    message = capsys.readouterr()
    assert message.out == 'Цена не должна быть нулевая или отрицательная\n'
    fix_product.price = 100
    assert fix_product.price == 100



