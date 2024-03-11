import sys

input = sys.stdin.readline
n = int(input())
meet = sorted([list(map(int, input().split())) for _ in range(n)])
ans = 0
i = 0
after = -1
while i < n:
    s, e = meet[i]
    if s >= after:
        ans += 1
        after = e

    elif e <= after:
        after = e

    i += 1


print(ans)
