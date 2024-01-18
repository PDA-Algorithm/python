import sys

s = sys.stdin.readline()
q = []
tmp = 1
cnt = 0

for i in range(len(s)):
  if s[i] == '(':
    tmp *= 2
    q.append(s[i])
  elif s[i] == '[':
    tmp *= 3
    q.append(s[i])
  elif s[i] == ')':
    if len(q) == 0 or q[-1] == '[':
      cnt = 0
      break
    if s[i-1] == '(':
      cnt += tmp
    q.pop()
    tmp //= 2
  elif s[i] ==']':
    if len(q) == 0 or q[-1] == '(':
      cnt = 0
      break
    if s[i-1] == '[':
      cnt += tmp
    q.pop()
    tmp //= 3

if len(q) == 0:
  print(cnt)
else:
  print(0)