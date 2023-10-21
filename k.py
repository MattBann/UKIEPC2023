n,m = map(int, input().split())

d = []
x = {}
for i in range(m):
    d.append(list(map(int,input().split())))
    x[d[i][1]] = d[i][0]

toRemove = []
for i in range(m):
    dep = d[i][1]
    while True:
        if dep in x and x[dep] != -1:
            dep = x[dep]
        else: break
        if dep == d[i][1]:
            toRemove.append(i)
            x[d[i][1]] = -1
            break

print(toRemove)
if len(toRemove) > n//2 : print("NO")
else:
    print("YES")
    print(m-len(toRemove))
    for i in range(m):
        if i not in toRemove:
            print(str(i+1)+ " ", end="")
    print()