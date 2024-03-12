n = int(input())
arr = list(map(int, input().split()))
s, e = 0, n - 1
ans_s, ans_e = 0, n - 1
ans = int(1e10)

while s < e:
    if ans > abs(arr[s] + arr[e]):
        ans = abs(arr[s] + arr[e])
        ans_s, ans_e = s, e
    if ans == 0:
        print(arr[s], arr[e])
        exit()
    if arr[s] + arr[e] > 0:
        e -= 1
    else:
        s += 1

print(arr[ans_s], arr[ans_e])
