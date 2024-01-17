import sys
N = int(sys.stdin.readline())
cnt  = 0

def stack(words):
  q = list()
  for word in words:
    if len(q) == 0:
      q.append(word)
    elif q[-1] == word:
      q.pop()
    else:
      q.append(word)
  return len(q)

for _ in range(N):
  words = sys.stdin.readline().strip()
  if stack(words) == 0:
    cnt += 1
print(cnt)