import sys

n = int(sys.stdin.readline())

straw = []
answer = 0

for _ in range(n):
  straw.append(int(sys.stdin.readline()))
straw.sort()

for i in range(len(straw)-1, 1, -1):
  if straw[i] < straw[i-1] + straw[i-2]:
    answer = straw[i] + straw[i-1] + straw[i-2]
    break

if answer == 0:
  print(-1)
else:
  print(answer)
