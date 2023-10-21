N, W = map(int, input().split())

for i in range(N):
    print(W+(i*((-1)**i)), 500+(i*((-1)**(i+1))))