class Counter:
    """Класс Counter используется для счета"""

    def __init__(self, initial_value: int) -> None:
        self.value = initial_value

    def inc(self) -> int:
        """Метод для увеличения счетчика на 1"""

        self.value += 1
        return self.value

    def dec(self) -> int:
        """Метод для уменьшения счетчика на 1"""

        self.value -= 1
        return self.value


class ReverseCounter(Counter):
    def inc(self) -> int:
        """Метод для уменьшения счетчика на 1"""

        self.value -= 1
        return self.value

    def dec(self) -> int:
        """Метод для увеличения счетчика на 1"""

        self.value += 1
        return self.value


def get_counter(number: int) -> Counter | ReverseCounter:
    """Функция для определения объекта класса"""

    if number >= 0:
        return Counter(number)
    return ReverseCounter(number)
