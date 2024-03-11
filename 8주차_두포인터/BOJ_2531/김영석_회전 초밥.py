N, d, k, c = map(int, input().split())  # 접시 수, 초밥 가지 수, 연속 수, 쿠폰번호
arr = [int(input()) for _ in range(N)]
arr += arr[:k]

cnt = [0] * (d + 1)
best = 0

for i in range(k):
    if not cnt[arr[i]]:
        best += 1
    cnt[arr[i]] += 1

now = best
if not cnt[c]:
    best += 1

for j in range(k, N + k):
    # 오른쪽 접시 카운트
    cnt[arr[j]] += 1
    if cnt[arr[j]] == 1:
        now += 1

    # 왼쪽 접시 제외
    cnt[arr[j - k]] -= 1
    if not cnt[arr[j - k]]:
        now -= 1

    # 쿠폰 번호 확인
    if cnt[c]:
        best = max(best, now)
    else:
        best = max(best, now + 1)

print(best)
