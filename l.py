from math import ceil

h1, d1, t1 = map(int, input().split())
h2, d2, t2 = map(int, input().split())

p1 = (ceil(h2 / d1) - 1) * t1
p2 = (ceil(h1 / d2) - 1) * t2

if p1 < p2:
    print('player one')
elif p2 < p1:
    print('player two')
else:
    print('draw')
