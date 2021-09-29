import math as m


# функция проверки корректности ввода
def prov(x):
    dig = "0123456789"
    if (len(x) <= 0) or (x[0] not in dig) or (len(x) == 2 and x[1] not in dig):
        print("Вы должны ввести число")
        exit()
    else:
        return x


# каждый раз когда пользователь вводит строку, программа вызывает функцию проверки
b = input("Длина первой стороны = ")
prov(b)

c = input("Длина второй стороны = ")
prov(c)

alpha = input("Угол между ними в градусах = ")
prov(alpha)


# конвертирую переменные из строк в вещественные числа
b = float(b)
c = float(c)
alpha = float(alpha)

a = b ** 2 + c ** 2 - (2 * b * c) * m.cos(alpha)
print("Длина третьей стороны = ", m.sqrt(a))
