dec2roman = zip(
    [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1],
    ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
)


class Number:
    def dec(self):
        return self

    def bin(self):
        self = bin(self)[2:]
        return self

    def roman(self):
        result = []
        for d, r in dec2roman:
            while self >= d:
                result.append(r)
                self -= d
        return ''.join(result)


print(Number.dec(2022))
print(Number.bin(2022))
print(Number.roman(2022))
