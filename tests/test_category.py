def test_category_init(fix_category_1, fix_category_2):
    assert fix_category_1.name == 'Смартфоны'
    assert fix_category_1.description == 'Смартфоны, как средство'

    assert fix_category_2.name == 'Телевизоры'
    assert fix_category_2.description == 'Современный телевизор'

    assert fix_category_1.category_count == 2
    assert fix_category_2.category_count == 2
    assert fix_category_1.product_count == 2
    assert fix_category_2.product_count == 2
