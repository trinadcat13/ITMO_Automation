def add(x, y):
    return x + y

print(add(1, 2))
print(add('lol_kek', '_cheburek'))

def arg(a, b, c=2, d = 3):
    return a+b+c+d

print(arg(2, 2))
print(arg(2, 2, 3, 5))

def range_arg(a, b , c, d):
    return a + ' ' + b + ' ' + c + ' ' + d

print(range_arg('1', '2', '3', '4'))
print(range_arg('1', '2', d = '3', c = '4'))

def fte(a = (1, 2, 3, 4)):
    return a[0]

print(fte())

def circ(r, pi = 3.14159):
    return pi * r ** 2

print(circ(2))
