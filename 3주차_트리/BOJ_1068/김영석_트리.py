from collections import deque

n = int(input())
lst = list(map(int, input().split()))
d = int(input())

ans = 0
child = [[] for _ in range(n)]

for i in range(n):
    if lst[i] == -1:
        root = i
    else:
        child[lst[i]].append(i)
 
if root == d:
    print(0)
    exit()    
    
q = deque([root])

while q:
    now = q.popleft()
    is_root = True
    for c in child[now]:
        if c != d:
            q.append(c)
            is_root = False
    if is_root:
        ans += 1
    
print(ans)