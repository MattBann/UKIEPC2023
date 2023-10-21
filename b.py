n, m, k = (int(x) for x in input().split())

state = [0] * (m + 1)
cost = [0] * (m + 1)

for i in range(k):
    p, c = (int(x) for x in input().split())
    # c -= 1
    if state[c] == 0:
        state[c] = p
    elif state[c] == p:
        cost[c] += 100
        state[c] = 0
    else:
        cost[c] += abs(state[c] - p)
        state[c] = 0

for i in range(1, m+1):
    if state[i] != 0:
        cost[c] += 100

print(" ".join(map(str, cost[1:])))