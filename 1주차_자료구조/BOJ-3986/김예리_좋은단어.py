import sys

answer = 0

n = int(input())
for i in range(n):
  stack = []
  word = list(sys.stdin.readline().strip())
  
  for j in word:
    if len(stack) > 0:
      if stack[-1] == j:
        stack.pop()
      else:
        stack.append(j)
    else:
      stack.append(j)
  
  if len(stack) == 0:
    answer+=1
  
print(answer)