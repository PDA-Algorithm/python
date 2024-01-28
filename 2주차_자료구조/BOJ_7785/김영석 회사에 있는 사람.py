import sys
from heapq import heappush as push, heappop as pop
input = sys.stdin.readline
print = sys.stdout.write
h = []
gone = []
ans = []
for _ in range(int(input())):
    name, action = input().split()
    if action[0] == 'e':
        push(h, name)
    
    else:
        push(gone, name)

while h and gone:
    if h[0] < gone[0]:
        ans.append(pop(h))
    else:
        pop(h)
        pop(gone)

while h:
    ans.append(pop(h))
    
for i in range(len(ans)-1,-1,-1):
    print(ans[i]+'\n')