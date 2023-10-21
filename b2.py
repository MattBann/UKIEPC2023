n, m, k = map(int, input().split())

d = {}
costs = {i:0 for i in range(1,m+1)}

for i in range(k):
    pi, ci = map(int, input().split())
    if ci in d and d[ci] != 0:
        if d[ci] == pi:
            costs[ci] += 100
        else:
            costs[ci] += abs(d[ci] - pi)
        d[ci] = 0
    else:
        d[ci] = pi

for i in d.keys():
    if d[i] == 0:
        continue
    costs[i] += 100

for i in sorted(costs.keys()):
    print(costs[i], end=" ")
print()