sq, st, c = map(int, input().split())

t = sq * 2
if st > 0 and c >= 2:
    t += (st * 2) + 3
    c -= 2

t += (c // 2) * 3

print(t)
