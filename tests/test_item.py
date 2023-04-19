"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item


class Item:
    discount = 1

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def apply_pay_rate(self, pay_rate):
        self.price *= pay_rate

    def total_price(self):
        return self.price * self.quantity

    def apply_pay_rate(self, pay_rate):
        if pay_rate < 0:
            raise ValueError("Pay rate cannot be negative")
        elif pay_rate > 1:
            raise ValueError("Pay rate cannot be greater than 1")
        else:
            self.price *= (1 - pay_rate)


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
