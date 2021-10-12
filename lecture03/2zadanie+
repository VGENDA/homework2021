N = int(input())

try:
    s = int(N)
except:
    print("Введите число")
    exit()

numbers = []
flags = []
i = 2
while i <= N:
    numbers.append(i)
    flags.append(False)
    i += 1

idx = 0

while idx < N//2:
    n = numbers[idx]
    i = idx + n
    while i < len(numbers):
        flags[i] = True
        i += n

    idx += 1
    while idx < len(flags) and flags[idx]:
        idx += 1

i = 0
while i < len(numbers):
    if flags[i]:
        i += 1
        continue
    print(numbers[i], end=" ")
    i += 1
