import sys
import heapq

max_heap=[]
min_heap=[]

problem=[[0 for col in range(2)] for row in range(100001)]

n = int(sys.stdin.readline())

for i in range(n) :
  p, l = map(int, sys.stdin.readline().split())
  heapq.heappush(max_heap, [-l, -p])
  heapq.heappush(min_heap, [l, p])
  problem[p][0]=l
  problem[p][1]=1

m = int(sys.stdin.readline())

for i in range(m) :
  order = sys.stdin.readline().split()
  if order[0] == "recommend":
    if order[1] == "1":
      while True:
        if problem[-max_heap[0][1]][0] != -max_heap[0][0] or problem[-max_heap[0][1]][1] == 0:
          heapq.heappop(max_heap)
        else : 
          break
      print(-max_heap[0][1])
    elif order[1] == "-1":
      while True:
        if problem[min_heap[0][1]][0] != min_heap[0][0] or problem[min_heap[0][1]][1] == 0:
          heapq.heappop(min_heap)
        else : 
          break
      print(min_heap[0][1])
  elif order[0] == "add" :
    problem[int(order[1])][0] = int(order[2]) # 0번째에는 난이도
    problem[int(order[1])][1] = 1 #1번째에는 실제 추천 여부 참
    heapq.heappush(max_heap, [-int(order[2]), -int(order[1])])
    heapq.heappush(min_heap, [int(order[2]), int(order[1])])
  elif order[0] == "solved" :
    problem[int(order[1])][1] = 0 #실제 추천 여부 거짓으로 만들기