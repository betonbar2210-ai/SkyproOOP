def test_products_init(fix_product):
    assert fix_product.name == "QLED 4K"
    assert fix_product.description == "Фоновая подсветка"
    assert fix_product.price == 100000
    assert fix_product.quantity == 101
