import random as r

file = open("task1.txt", 'rt')

a = []

for line in file:
    a.append(int(line))


sum = 0
while sum != 2020:
    s1 = a[r.randint(0, 199)]
    s2 = a[r.randint(0, 199)]
    s3 = a[r.randint(0, 199)]
    sum = s1 + s2 + s3
    rez = s1 * s2 * s3


print(s1, '+', s2, '+', s3, '=', sum)
print(s1, '*', s2, '*', s3, '=', rez)

file.close()

f = open('output1.txt', 'w')
f.write(str(rez))
print("Результат записан")
f.close()
