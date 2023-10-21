n,c = map(int, input().split())
ds = list(map(int, input().split()))

for i in range(n):
    if ds[i] > c:
        ds[i] = c

s = sum(ds)
answers = []
for i in range(n):
    x = s - (ds[(i-1) % n])
    answers.append(str(x // c))
print(" ".join(answers))