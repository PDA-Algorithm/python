from heapq import heappop as pop, heappush as push
import sys
input = sys.stdin.readline
print = sys.stdout.write
h = []
for _ in range(int(input())):
    i = int(input())
    if not i:
        if h:
            print(str(-pop(h)) + '\n')
        else:
            print('0\n')
    else:
        push(h, -i)