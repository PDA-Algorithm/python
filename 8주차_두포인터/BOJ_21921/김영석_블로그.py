n, x = map(int, input().split())
arr = list(map(int, input().split()))
best = now = sum(arr[:x])
cnt = 1
for i in range(n - x):
    now += arr[x + i] - arr[i]
    if best > now:
        continue
    elif best == now:
        cnt += 1
    else:
        best = now
        cnt = 1
if not best:
    print("SAD")
    exit()
print(best)
print(cnt)
