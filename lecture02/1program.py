import string as s

print("Введите число от 0 до 99")

num = input()
res = ""

if (len(num) <= 0 or len(num) > 2) or (num[0] not in s.digits) or (len(num) == 2 and num[1] not in s.digits):
    print("Вы должны ввести число от 0 до 99")
else:
    if num[-1] == "0" and len(num) == 1:
        res = "ноль"
    if num[-1] == "1":
        res = "один"
    if num[-1] == "2":
        res = "два"
    if num[-1] == "3":
        res = "три"
    if num[-1] == "4":
        res = "четыре"
    if num[-1] == "5":
        res = "пять"
    if num[-1] == "6":
        res = "шесть"
    if num[-1] == "7":
        res = "семь"
    if num[-1] == "8":
        res = "восемь"
    if num[-1] == "9":
        res = "девять"

    if len(num) == 2:
        if num == "10":
            res = "десять"
        if num == "11":
            res = "одиннадцать"
        if num == "12":
            res = "двенадцать"
        if num == "13":
            res = "тринадцать"
        if num == "14":
            res = "четырнадцать"
        if num == "15":
            res = "пятнадцать"
        if num == "16":
            res = "шестнадцать"
        if num == "17":
            res = "семнадцать"
        if num == "18":
            res = "восемнадцать"
        if num == "19":
            res = "девятнадцать"

        if num[0] == "2":
            res = "двадцать " + res
        if num[0] == "3":
            res = "тридцать " + res
        if num[0] == "4":
            res = "сорок " + res
        if num[0] == "5":
            res = "пятьдесят " + res
        if num[0] == "6":
            res = "шестьдесят " + res
        if num[0] == "7":
            res = "семьдесят " + res
        if num[0] == "8":
            res = "восемьдесят " + res
        if num[0] == "9":
            res = "девяноста " + res

    print(res)
