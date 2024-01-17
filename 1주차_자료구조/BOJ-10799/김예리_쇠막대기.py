import sys

stack =[]
answer = 0

stick = sys.stdin.readline().strip()

for i in range(len(stick)):
  if stick[i] == '(':
    stack.append(i)
  else: # stick[i] == ')'
    stack.pop()
    if stick[i-1] == '(':
      answer += len(stack)
    else: # 연속으로 닫으면 끊긴 막대 하나 추가
      answer += 1

print(answer)

