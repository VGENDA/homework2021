class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'z = {self.a + other.a} + {self.b + other.b}j'

    def __sub__(self, other):
        return f'z = {self.a - other.a} + {self.b - other.b}j'

    def __mul__(self, other):
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a}j'


# декорации
arg1 = int(input('Действительная часть первого комплексного числа: '))
arg2 = int(input('Мнимая часть первого комплексного числа: '))
arg3 = int(input('Действительная часть второго комплексного числа: '))
arg4 = int(input('Мнимая часть второго комплексного числа: '))

z_1 = Complex(arg1, arg2)
z_2 = Complex(arg3, arg4)

print('Сложение: ', z_1 + z_2)
print('Вычитание: ', z_1 - z_2)
print('Умножение: ', z_1 * z_2)
