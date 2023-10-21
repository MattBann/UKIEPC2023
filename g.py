import math

def add(a, b):
    x1, y1 = a
    x2, y2 = b
    return (x1 + x2, y1 + y2)

def sub(a, b):
    x1, y1 = a
    x2, y2 = b
    return (x2 - x1, y2 - y1)

def mul(a, x):
    return (a[0] * x, a[1] * x)

def dot(a, b):
    x1, y1 = a
    x2, y2 = b
    return x1 * x2 + y1 * y2

def distance(a, b):
    d = sub(b, a)
    return math.sqrt(dot(d, d))

s = float(input())
n = int(input())
points = []
for i in range(n):
    x, y = [int(x) for x in input().split()]
    points.append((x, y))

cd = 0
i1 = 0
i2 = 0
for i in range(n - 1):
    d = distance(points[i], points[i + 1])
    cd += d
    if cd > s:
        i2 = i
        break

dmin = 99999999

while True:
    if i1 == i2:
        d = s
    else:
        a1 = points[i1]
        b1 = points[i1 + 1]
        a2 = points[i2]
        b2 = points[i2 + 1]

        alpha = sub(add(a1, b2), add(a2, b1))
        T = dot(alpha, sub(a1, a2)) / dot(alpha, alpha)

        

        p1 = add(a1, mul(sub(b1, a1), T))
        p2 = add(a2, mul(sub(b2, a2), T))

        d = distance(p1, p2)

    if d < dmin:
        dmin = d


# a1 = points[0]
# b1 = points[1]
# a2 = points[0]
# b2 = points[1]
# alpha = sub(add(a1, b2), add(a2, b1))
# print(alpha)
# T = dot(alpha, sub(a1, a2)) / dot(alpha, alpha)