import sys

str = sys.stdin.readline().strip()

stack = []
answer = 0 # 최종 정답
tmp = 1

for i in range(len(str)):
  if str[i] == "(":
    stack.append(str[i])
    tmp*=2
  elif str[i] == "[":
    stack.append(str[i])
    tmp*=3
  
  elif str[i] == ")":
    if len(stack) == 0 or stack[-1] == "[":
      answer = 0
      break
    else: # 예외 상황 아닐 때
      if str[i-1] == "(":
        answer+=tmp 
      stack.pop()
      tmp//=2 # tmp 다시 돌려놓기
  
  elif str[i] == "]":
    if len(stack) == 0 or stack[-1] == "(":
      answer = 0
      break
    else: # 예외 상황 아닐 때
      if str[i-1] == "[":
        answer+=tmp 
      stack.pop()
      tmp//=3 # tmp 다시 돌려놓기

if len(stack)==0:
  print(answer)
else:
  print(0)