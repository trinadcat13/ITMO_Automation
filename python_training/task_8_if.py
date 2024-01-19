num = 3

if num >= 0:
    print('Число больше либо равно 0')
else:
    print('Число отрицательное')

str_1 = 'test'
str_2 = 'test1'

if str_1 in str_2:
    print('Да')
else:
    print('Нет')

num_float = -3.4

if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Отрицательное число')

permit_print = True

if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')

def student_rank(year_of_study):
    if year_of_study in range(5, 7):
        print('Вы - бакалавр')
    elif year_of_study in range(5, 7):
        print('Вы - магистрант')
    elif year_of_study in range(7, 10):
        print('Вы - аспирант')
    else:
        print('Введите корректный год обучения')

student_rank(2)

a = 5

if a > 100 or a < -100:
    print('-')
else:
    print('+')