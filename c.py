import math

n = int(input())
p = int(input())
ns = list(map(float, input().split()))

ms= []
for i in range(n):
    ms.append([(ns[(i-1) % n] + ns[(i+1) % n]) - ns[i], i])

ms.sort(reverse=True, key=lambda x : x[0])

sum = 0.0

for i in range(0,p):
    sum += math.sin(ns[ms[i][1]] - ns[ms[i-1 % n][1]])
    sum += math.sin(ns[ms[i+1 % n][1]] - ns[ms[i][1]])

print(sum)