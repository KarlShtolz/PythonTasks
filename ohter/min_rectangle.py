"""
На клетчатой плоскости закрашено K клеток. Требуется найти минимальный по площади прямоугольник, со сторонами,
параллельными линиям сетки, покрывающий все закрашенные клетки.

INPUT:
3
1 1
1 10
5 5
OUTPUT:
1 1 5 10

"""

n = int(input())
x = []
y = []
for i in range(n):
    s = input()
    z = s.split(" ")
    x.append(int(z[0]))
    y.append(int(z[1]))
    z = []
print(min(x), min(y), max(x), max(y), sep=" ")