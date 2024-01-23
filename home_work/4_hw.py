# Задача 1
class rect:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def ploshad(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2


obj_0 = rect(2, 2)

obj_1 = rect(5, 5)

obj_2 = rect(3, 3)

print('Площадь', obj_0.ploshad(), 'Периметр', obj_0.perimeter())

print('Площадь', obj_1.ploshad(), 'Периметр', obj_1.perimeter())

print('Площадь', obj_2.ploshad(), 'Периметр', obj_2.perimeter())

# Задача 2
class math:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b


    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

    def subtraction(self):
        return self.a - self.b


obj_3 = math(8, 5)

print('Сложение:', obj_3.addition(), 'Умножение:', obj_3.multiplication(),
      'Вычитание:', obj_3.division(), 'Деление:', obj_3.subtraction())


# Задача 3
class ButtonThree:
    type = 'Кнопка'
    loc: str

class B4(ButtonThree):

    def __init__(self, text):
        self.text = text

    def click(self):
        return 'Клик по кнопке "{}"'. format(self. text)

butt_0 = B4('Текстовое окно')
butt_1 = B4('Флажок')
butt_2 = B4('Переключатель')
butt_3 = B4('Веб-таблицы')
butt_4 = B4('Кнопки')
butt_5 = B4('Ссылки')
butt_6 = B4('Неработающие ссылки - изображения')
butt_7 = B4('Загрузить и скачать')
butt_8 = B4('Динамические свойства')


print(butt_0.click())
print(butt_1.click())
print(butt_2.click())
print(butt_3.click())
print(butt_4.click())
print(butt_5.click())
print(butt_6.click())
print(butt_7.click())
print(butt_8.click())

