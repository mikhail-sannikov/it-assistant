import locale

from calendar import month_name
from typing import Any

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')


def date_conversion(day: int, month: int, year: int) -> str:
    """Функция преобразует даты

    Функция принимает на вход три целых числа в следующем порядке:
    день, месяц, год и возвращает строку формата:
    день(число) месяц(название) год(число) года

    Arguments:
        day - день
        month - номер месяца
        year - год

    """

    names_of_months = tuple(name.replace(name[-1], 'я')
                            if name != 'Март' and name != 'Август'
                            else f'{name.lower()}а'
                            for name in month_name[1:])
    return f'{day} {names_of_months[month - 1].lower()} {year} года'


def names_counter(names: tuple[str]) -> dict[str: int]:
    """Функция считает сколько раз встретилось имя

    Функция принимает на вход кортеж строк (имена) и возвращает словарь,
    в котором будет указано, какое имя сколько раз встречалось в кортеже

    Arguments:
        names - кортеж строк (имена)

    """

    counter = {}
    for name in names:
        counter[name] = counter.get(name, 0) + 1
    return counter


def data_conversion(human_data: dict[str: str]) -> str:
    """Функция преобразует данные о человеке

    Функция принимает на вход словарь,
    в котором находятся данные о человеке в формате:
    {'first_name': 'Имя', 'last_name': 'Фамилия', 'middle_name': 'Отчество'}
    Функция возвращает данные о человеке в виде
    строки формата 'Фамилия Имя Отчество'.
    Данные в словаре могут быть неполными,
    тогда возвращаемая строка определяется рядом условий

    Arguments:
        human_data - словарь с данными человека в формате
        {'first_name': 'Имя',
         'last_name': 'Фамилия',
         'middle_name': 'Отчество'}

    """

    result = ''

    if ('last_name' not in human_data
            and 'first_name' in human_data
            and 'middle_name' in human_data):
        result = f'{human_data['first_name']} {human_data['middle_name']}'

    elif ('middle_name' not in human_data
          and len(human_data) >= 1):
        result = ' '.join(reversed(human_data.values()))

    elif ('first_name' not in human_data
          and 'last_name' in human_data
          and 'middle_name' in human_data):
        result = f'{human_data['last_name']}'

    elif (('middle_name' in human_data and len(human_data) == 1)
          or len(human_data) == 0):
        result = 'Нет данных'

    return result


def is_a_simple_number(number: int) -> bool:
    """Функция определдяет простое число или нет

    Функция принимает на вход число и возвращает True,
    если число простое (делится только на себя и на 1),
    и False, если число составное

    Arguments:
        number - число для проверки

    """

    check = True
    for i in range(2, number):
        if number % i == 0:
            check = False
    return check


def unique_numbers(*args: Any) -> list[int | float]:
    """Функция для отбора уникальных чисел

       Функция принимает на вход произвольное количество
       аргументов разных типов - числа, строки, булевы типы, None
       и возвращает список, в который войдут все уникальные числа,
       встреченные во входящих аргументах, в возрастающем порядке.

       Arguments:
           args - произвольное количество аргументов разных типов данных

    """

    return sorted([i for i in set(args)
                   if (isinstance(i, int) or isinstance(i, float))
                   and not isinstance(i, bool)])
