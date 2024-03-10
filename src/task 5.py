#Программа, которая получает на вход три целых числа, по одному числу в строке, и выводит на консоль в три строки сначала максимальное, потом минимальное, после чего оставшееся число.

a = int(input())
b = int(input())
c = int(input())
max = 0
min = 0

if a >= b and a >= c:
    max = a
elif b >= a and b >= c:
    max = b
elif c >= a and c >= a:
    max = c

if a <= b and a <= c:
    min = a
elif b <= a and b <= c:
    min = b
elif c <= a and c <= a:
    min = c

print(max)
print(min)

mid = 0

if max != b and b != min:
    mid = b
elif a != max and a != min:
    mid = a
elif max != c and min != c:
    mid = c
elif a == c:
    mid = a
elif a == b:
    mid = a
elif b == c:
    mid = b

print(mid)