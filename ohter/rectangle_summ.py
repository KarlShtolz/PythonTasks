"""
Вам необходимо ответить на запросы узнать сумму всех элементов числовой матрицы N×M в прямоугольнике с левым верхним
углом (x1, y1) и правым нижним (x2, y2)

INPUT:
3 3 2
1 2 3
4 5 6
7 8 9
2 2 3 3
1 1 2 3
OUTPUT:
28
21
"""

n, m, k = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
b = [[0 for j in range(m+1)] for i in range(n+1)]

for i in range(n):
    for j in range(m):
        b[i + 1][j + 1] = a[i][j] + b[i][j + 1] + b[i + 1][j] - b[i][j]

x = []
for i in range(k):
    i1, j1, i2, j2 = map(int, input().split())
    c = b[i2][j2] - b[i1 - 1][j2] - b[i2][j1 - 1] + b[i1 - 1][j1 - 1]
    x.append(c)
print(*x, sep='\n')