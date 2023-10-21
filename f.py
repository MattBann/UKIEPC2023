n, c = [int(x) for x in input().split()]
d = [int(x) for x in input().split()]

def func(i):
    time = 0
    ads = 0
    for j in range(n):
        song = (j + i) % n
        time += d[song]
        if time >= c and j < n - 1:
            time = 0
            ads += 1
    return ads

for i in range(n):
    print(func(i), end=' ')

print()