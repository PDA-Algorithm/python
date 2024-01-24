# #시간초과
# import sys

# prob = dict()

# n = int(input())
# for i in range(n):
#   p, l = map(int, input().split())
#   prob[p] = l

# m = int(input())
# for i in range(m):
#   order = list(sys.stdin.readline().split())
#   if order[0] == 'add' :
#     prob[int(order[1])] = int(order[2])
#   elif order[0] == 'recommend' :
#     #tmp = sorted(prob.items(), key = lambda item : item[1])
#     if order[1] == '1':
#       #print(tmp[-1][0])
#       for k, v in prob.items():
#         if v == max(prob.values()):
#           print(k)
#       #print(max(prob.values())[0])
#     else:
#       for k, v in prob.items():
#         if v == min(prob.values()):
#           print(k)
#   elif order[0] == 'solved' :
#     del prob[int(order[1])]


# 2.
# 리스트 인덱스가 문제 번호고 리스트에다가 난이도랑 실제 추천 여부를 저장
# 추천할 때 리스트에서 실제 추천 여부 검사와 실제 난이도 검사가 둘 다 참
# Add 할 때는 리스트에다가 난이도랑 실제 추천을 참으로 넣고,
# 힙에다가도 난이도랑 문제 추가
# Solved 할 때는 리스트 실제 추천 여부를 거짓으로 하고,
# 추천할 때 실제 추천 여부 검사가 거짓일 때만 힙에서 pop
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
  order = sys.stdin.readline().rstrip().split()
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

