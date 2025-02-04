a = input("Введите символ: ")
b = 0
c = int(input("Введите размер пирамиды: "))
for i in range(c):
    b += 1
    print(a * b)

a = int(input("Введите сумма вклада(долга): "))
b = int(input("Введите процент: "))
c = int(input("Введите срок вклада(долга): "))
d = a
for i in range(c):
    d += a * (b / 100)
print(d)

a = int(input("Введите сумма вклада(долга): "))
b = int(input("Введите процент: "))
c = int(input("Введите срок вклада(долга): "))
for i in range(c):
    a = a + a * (b / 100)
print(a)

a = input("Введите символ: ")
b = int(input("Введите размер пирамиды: "))
while b > 0:
    b -= 1
    print(a * b)

a = int(input("Введите число(от 0 до 100): "))
if a > 100 or a < 0:
    print('Число не подходит')
else:
    while a < 100:
        a += 1
        print(a)

import random

print("Попытайтесь угадать цифру:")
a = int(input())
b = random.randint(1, 9)
while a != b:
    print("Не угадали")
    a = int(input())
print("Угадали")