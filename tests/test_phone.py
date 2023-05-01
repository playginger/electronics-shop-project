import pytest
from src.phone import Phone
from src.item import Item


@pytest.fixture
def phone():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_methods():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_add():
    item1 = Item("Смартфон", 10000, 20)
    phone = Phone("iPhone 14", 120_000, 5, 2)
    assert item1 + phone == 25
    assert phone + phone == 10


def test_setter(phone):
    assert phone.number_of_sim == 2
    with pytest.raises(ValueError):
        phone.number_of_sim = 0
