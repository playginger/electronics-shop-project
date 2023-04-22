import csv


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

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_):
        if len(name_) <= 10:
            self.__name = name_
        else:
            print('Длина наименования товара превышает 10 символов')

    @classmethod
    def instantiate_from_csv(cls):
        with open('../src/items.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for word in reader:
                cls.all.append(cls(word['name'], word['price'], word['quantity']))

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
            raise ValueError("Pay rate cannot be negative")
        elif pay_rate > 1:
            raise ValueError("Pay rate cannot be greater than 1")
        else:
            self.price *= (1 - pay_rate)
