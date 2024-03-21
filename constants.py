from enum import Enum

BASE_URL = 'https://www.google.com/search?q=калькулятор'


class Operation(Enum):
    minus = '-'
    plus = '+'
    divide = '/'
    multiply = '*'


# Соответствие номеров калькулятора и номеров в массиве элементов
numbers_equals = {
    0: 9,
    1: 6,
    2: 7,
    3: 8,
    4: 3,
    5: 4,
    6: 5,
    7: 0,
    8: 1,
    9: 2,
}
