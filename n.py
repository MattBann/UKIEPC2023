def name_gen():
    word = list('aaaaaaaaaaa')
    while True:
        yield ''.join(word)
        prev_index = len(word) - 1
        while prev_index >= 0:
            if word[prev_index] < 'z':
                word[prev_index] = chr(ord(word[prev_index]) + 1)
                break
            else:
                word[prev_index] = 'a'
                prev_index -= 1
        if prev_index < 0:
            word.append('a')

n = int(input())

bottles = []
for i in range(n):
    v = input()
    v = v[:-1]
    if '.' not in v:
        v += '.0'
    a, b = v.split('.')
    v = f'{int(a)}.{str(int(b[::-1]))[::-1]}'
    bottles.append(v)

gen = name_gen()
bottle_names = {}
def func(s):
    if s in bottle_names:
        return bottle_names[s]
    bottle_names[s] = next(gen)
    return bottle_names[s]

for x in bottles:
    print(func(x))
