N, K = map(int, input().split())
arr = list(map(int, input().split()))
cnt = [0] * 100001
s = 0
best_len = 0
for i in range(N):
    if cnt[arr[i]] < K:
        cnt[arr[i]] += 1
    else:
        best_len = max(best_len, i - s)
        while arr[s] != arr[i]:
            cnt[arr[s]] -= 1
            s += 1
        s += 1
print(max(best_len, i - s + 1))
