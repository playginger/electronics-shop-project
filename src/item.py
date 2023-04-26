import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    discount = 1

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.__class__.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_):
        if len(name_) <= 10:
            self.__name = name_
        else:
            raise ValueError('Длина наименования товара превышает 10 символов')

    @classmethod
    def instantiate_from_csv(cls):
        cls.all = []
        with open(
                os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')), 'src', 'items.csv')) as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                name = row[0]
                price = float(row[1])
                quantity = int(row[2])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(number):
        return int(float(number))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity * self.pay_rate

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    def total_price(self):
        return self.price * self.quantity

    def apply_pay_rate(self, pay_rate):
        if pay_rate < 0:
            raise ValueError("Ставка оплаты не может быть отрицательной")
        elif pay_rate > 1:
            raise ValueError("Ставка оплаты не может быть больше 1")
        else:
            self.price *= (1 - pay_rate)
