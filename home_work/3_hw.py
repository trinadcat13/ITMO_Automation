# Задача 2
def max(a, b):
    if a >= b:
        return a
    else:
        return b


print('Большее число:', max(5 , 7 ))

# Задача 3
def much(a, b):
    if abs(a-b) > 135:
        print('Yes')
    else:
        print('No')
    return()


much(22,600)


# Задача 4
def month(a):
    if a in range(1 , 3) or a == 12:
        print('Сезон года - зима')
    elif a in range(3 , 6):
        print('Сезон года - весна')
    elif a in range(6 , 9):
        print('Сезон года - лето')
    elif a in range(9 , 12):
        print('Сезон года - осень')
    else:
        print('Нет такого месяца, введите нармальна')
    return()


month(1)

# Задача 5
def ten(a, b, c):
    if a > 10 and b>10 and c>10:
        print ('YES')
    else:
        print ('No')
    return ()

ten(5, 10,29)


# Задача 6
def pos(a: list):
    print (len([x for x in a if x > 0]))

pos([5, 10, -15, -29, -30])


# Задача 7
def days(year: int, month: int):
    print(((year * 12) + month) * 29)

days(3, 4)