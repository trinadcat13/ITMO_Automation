def task_1() -> tuple:
    a: int = 1
    b: float = 3.14
    c: str = 'M&Ms'
    d: list = [3, 2]
    e: bool = False
    return a, b, c, d, e


print(task_1())


def task_2() -> list:
    a = [1, 2, 3, 5, 8, 13, 21]
    return (a[0:3])


print('Это вроде бы диапазон или "срез" списка:', task_2())


def sqr(a: float) -> float:
    return a ** 2


print('Квадрат числа "5" - это опять', sqr(5) )
