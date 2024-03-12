import sys

input = sys.stdin.readline

n, k = map(int, input().split())
num = input().strip() # 맨 끝 줄바꿈 제거

stack = []
cnt = 0

for n in num:
  while stack and stack[-1] < n and cnt!=k:
    stack.pop()
    cnt+=1
  stack.append(n)

# k개를 지우지 않았을 때 처리
if cnt!=k:
  print("".join(stack[:-(k-cnt)]))
else:
  print("".join(stack))
