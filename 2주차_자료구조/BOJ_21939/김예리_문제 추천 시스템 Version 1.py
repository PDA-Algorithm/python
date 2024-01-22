#시간초과
import sys

prob = dict()

n = int(input())
for i in range(n):
  p, l = map(int, input().split())
  prob[p] = l

m = int(input())
for i in range(m):
  order = list(sys.stdin.readline().split())
  if order[0] == 'add' :
    prob[int(order[1])] = int(order[2])
  elif order[0] == 'recommend' :
    #tmp = sorted(prob.items(), key = lambda item : item[1])
    if order[1] == '1':
      #print(tmp[-1][0])
      for k, v in prob.items():
        if v == max(prob.values()):
          print(k)
      #print(max(prob.values())[0])
    else:
      for k, v in prob.items():
        if v == min(prob.values()):
          print(k)
  elif order[0] == 'solved' :
    del prob[int(order[1])]

