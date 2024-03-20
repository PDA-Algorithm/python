import sys
input = sys.stdin.readline

n, d, k, c = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
cnt=0
for i in range(0,n):
    start = i
    end = (i+(k-1))%n
    temp = []
    if start > end:
        temp = arr[start:]
        for val in arr[:end+1]:
            temp.append(val)
        temp.append(c)
    else:
        temp = arr[start:end+1]
        temp.append(c)
    lst = set(temp)
    # print(lst)
    cnt = max(cnt, len(lst))

print(cnt)
