n=int(input())
dict = {}
for _ in range(n):
    a, b = input().split()
    if dict.get(a) == None:
        dict[a] = 1
    else:
        del dict[a]

result = sorted(dict.keys(), reverse=True)
for d in result:
    print(d)
