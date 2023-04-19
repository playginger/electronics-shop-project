"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item


def __init__(self, price, quantity):
    self.price = price
    self.quantity = quantity


def total_cost(self):
    return self.price * self.quantity


def apply_pay_rate(self, pay_rate):
    if pay_rate < 0:
        raise ValueError("Pay rate cannot be negative")
    elif pay_rate > 1:
        raise ValueError("Pay rate cannot be greater than 1")
    else:
        self.price *= (1 - pay_rate)


if __name__ == '__main__':
    def test_total_cost():
        item1 = Item("Смартфон", 10000, 20)
        item2 = Item("Ноутбук", 20000, 5)
        assert item1.total_cost() == 15
        assert item2.total_cost() == 10


    def test_apply_pay_rate():
        Item.discount = 0.9  # установка скидки на все товары
        item1 = Item("Смартфон", 10000, 20)
        item2 = Item("Ноутбук", 20000, 5)

        assert item1.price == 1.35
        assert item2.price == 2


    def test_apply_pay_rate_negative_pay_rate():
        Item.discount = -0.1  # отрицательная скидка
        item1 = Item("Смартфон", 10000, 20)
        item2 = Item("Ноутбук", 20000, 5)
        item1.apply_pay_rate()
        assert item1.price == -0.15
        assert item2.price == -2


    def test_apply_pay_rate_positive_pay_rate():
        Item.pay_rate = 1.5  # положительный коэффициент оплаты
        item1 = Item("Смартфон", 10000, 20)
        item2 = Item("Ноутбук", 20000, 5)
        item1.apply_pay_rate()
        assert item1.price == 22500
        assert item2.price == 45000
