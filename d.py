count = input()
strengths = list(map(int, input().split(' ')))

strengths.sort(reverse=True)
strengths = strengths[1:int(len(strengths) * 2/3):2]
total = sum(strengths)
print(total)
