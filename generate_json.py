import json
from pprint import pprint
from typing import NoReturn


class Shop_list:
    def __init__(self, title, category, quantity, price, surname):
        self.title = title
        self.category = category
        self.quantity = quantity
        self.price = price
        self.surname = surname

    def __repr__(self):
        return f'"{self.title}", "{self.category}", "{self.quantity}", "{self.price}", "{self.price}", "{self.surname}"'

    def __str__(self):
        return f'Title: {self.title}, category: {self.category}, quantity: {self.quantity}, price: {self.price}, surname: {self.surname}'


def generate_purchase():
    phone = {
        'title': 'Iphone10',
        'category': 'electronics',
        'quantity': '2',
        'price': '100',
        'surname': 'Kruts'
    }
    phone_obj = Shop_list(**phone)

    dress = {
        'title': 'cocktail dress',
        'category': 'clothes',
        'quantity': '1',
        'price': '10',
        'surname': 'Tymenko'
    }
    apple = {
        'title': 'apple',
        'category': 'friut',
        'quantity': '20',
        'price': '2',
        'surname': 'Ovcharenko'
    }
    water = {
        'title': 'still water',
        'category': 'drinks',
        'quantity': '5',
        'price': '2',
        'surname': 'Sviridenko'
    }
    lipstick = {
        'title': 'lipstick',
        'category': 'cosmetics',
        'quantity': '1',
        'price': '1',
        'surname': 'Vasilenko'
    }
    purchase = [
        phone,
        dress,
        apple,
        water,
    ]
    with open('shop_list.json', 'w') as f:
        json.dump(purchase, f, indent=2)


def get_purchase() -> NoReturn:
    with open('shop_list.json') as f:
        for i in json.load(f):
            pprint(f'{Shop_list(**i)!r}')


if __name__ == '__main__':
    generate_purchase()
    get_purchase()
