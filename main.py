import locale

from calendar import month_name

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')


def date_conversion(day: int, month: int, year: int) -> str:
    """Функция принимает на вход три целых числа в следующем порядке: день, месяц, год
    и возвращает строку формата: день(число) месяц(название) год(число) года"""

    names_of_months = tuple(name.replace(name[-1], 'я')
                            if name != 'Март' and name != 'Август' else f'{name.lower()}а'
                            for name in month_name[1:])
    return f'{day} {names_of_months[month-1].lower()} {year} года'
