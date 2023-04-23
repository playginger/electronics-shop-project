"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item


def test_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1.total_price() == 200000
    assert item2.total_price() == 100000


def test_apply_pay_rate():
    Item.discount = 0.9  # установка скидки на все товары
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1.price == 10000  # ожидаемая цена со ставкой оплаты
    assert item2.price == 20000  # ожидаемая цена со ставкой оплаты


def test_apply_pay_rate_negative_pay_rate():
    Item.discount = -0.1  # отрицательная скидка
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    item1.apply_pay_rate(0.1)
    assert item1.price == 9000
    assert item2.price == 20000


def test_apply_pay_rate_positive_pay_rate():
    Item.pay_rate = 0.5  # положительный коэффициент оплаты
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    item1.apply_pay_rate(Item.pay_rate)  # передать pay_rate как аргумент
    assert item1.price == 5000 and item2.price == 20000


def test_name_setter():
    item = Item('СуперСмартфон', 10000, 1)
    item.name = 'Ноутбук'
    assert item.name == 'СуперСмартфон'


def test_instantiate_from_csv():
    item1 = Item('Смартфон', 10000, 1)
    item1.instantiate_from_csv()
    assert len(Item.all) == 20
    assert Item.all[0].name == 'Смартфон'


def test_string_to_number():
    item = Item('Смартфон', 10000, 1)
    assert isinstance(item.string_to_number(item.quantity), int)
