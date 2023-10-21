n,m = map(int, input().split())
d = []
x = {}
for i in range(m):
    a = tuple(map(int, input().split()))
    if a in d:
        x[a] += 1
    else:
        d.append(a)
        x[a] = 1
removed = []
for i in range(1,n+1):
    prevs = {}
    ttl = m
    first = True
    s = [i]
    while len(s) > 0 and ttl >= 0:
        node = s.pop()
        ttl -= 1
        for dep in d:
            if dep[0] == node:
                s.append(dep[1])
                prevs[dep[1]] = node
        if node == i and not first:
            bestc, best = m, None
            current = i
            while True:
                for k in range(len(d)):
                    if d[k][1] == current and d[k][0] == prevs[current]:
                        if x[d[k]] < bestc:
                            bestc = x[d[k]]
                            best = d[k]
                current = prevs[current]
                if current == i:
                    ttl = 0
                    break
            for k in range(len(d)):
                if d[k] == best:
                    d.pop(k)
                    removed.append(k+1)
        first = False

if len(removed) > n//2 : print("NO")
else:
    print("YES")
    print(m-len(removed))
    for i in range(m):
        if i not in removed:
            print(str(i+1)+ " ", end="")
    print()