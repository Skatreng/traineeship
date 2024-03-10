#Программа для подсчета жилплощади комнат в зависимости от типа фигуры комнаты. На вход подаётся тип фигуры комнаты и соответствующие параметры.
#Для числа π используют значение 3.14.

import math

shape = input()

if shape == "треугольник":
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) / 2
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(S)
elif shape == "прямоугольник":
    a = float(input())
    b = float(input())
    print(a * b)
elif shape == "круг":
    r = float(input())
    p = 3.14
    print(p * r * r)
