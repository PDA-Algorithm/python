import sys

input = sys.stdin.readline
n = int(input())
num = [0] * (1000001)
for _ in range(n):
    num[int(input())] += 1

selected = []

i = 1000000
while i > 0:
    if not num[i]:
        i -= 1
        continue

    elif len(selected) <= 1:
        selected.append(i)
        num[i] -= 1
        continue

    elif selected[0] >= selected[1] + i:
        selected.pop(0)
        continue

    else:
        print(sum(selected) + i)
        exit()

print(-1)
