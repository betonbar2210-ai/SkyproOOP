from src.lawngrass import LawnGrass
from src.products import Product
from src.smartphone import Smartphone


def test_print_mixin(fix_product, capsys):
    Product(name="QLED 4K", description="Фоновая подсветка", price=100000, quantity=101)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(QLED 4K, Фоновая подсветка, 100000 ,101 шт.)"


def test_print_smartphone(capsys):
    Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 2, 95.5, "S23 Ultra", 256, "Серый"
    )
    message = capsys.readouterr()
    assert (
        message.out.strip() == "Smartphone(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0 ,2 шт.)"
    )


def test_print_lawngrass(capsys):
    LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 1, "США", "5 дней", "Темно-зеленый")
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass(Газонная трава 2, Выносливая трава, 450.0 ,1 шт.)"
