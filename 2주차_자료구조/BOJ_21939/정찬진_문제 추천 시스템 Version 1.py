import sys
import heapq

N = int(sys.stdin.readline())
min_heap = []
max_heap = []
check = dict()
for i in range(N):
  num, val = map(int,sys.stdin.readline().split())
  heapq.heappush(min_heap,(val,num))
  heapq.heappush(max_heap,(-val,-num)) # 문제번호와 난이도에 전부 음수처리해서 난이도가 같을 경우 1이 들어오면 문제번호가 큰 순서대로 출력
  check[num] = 1 # 존재한다는 의미로 {문제번호 : 1} 형식으로 저장 
T = int(sys.stdin.readline())
for j in range(N,N+T):
  op = list(sys.stdin.readline().split())

  if op[0] == 'add':
    heapq.heappush(min_heap,(int(op[2]),int(op[1])))
    heapq.heappush(max_heap,(-int(op[2]),-int(op[1])))
    if check.get(int(op[1])) == None: # 중복 처리를 위해 값이 처음부터 없으면 1로 저장
      check[int(op[1])] = 1
    else: # 중복처리를 위해 이미 들어왔던 값이지만 solved해서 0이 된 경우 +1
      check[int(op[1])] += 1
      
  elif op[0] == 'recommend':
    dec = int(op[1])
    if dec == 1:
      while max_heap and check[-max_heap[0][1]] == 0: # 출력하려는 값이 이미 solved된 경우 삭제
        heapq.heappop(max_heap)
      print(-max_heap[0][1])
    else:
      while min_heap and check[min_heap[0][1]] == 0: # 출력하려는 값이 이미 solved된 경우 삭제
        heapq.heappop(min_heap)
      print(min_heap[0][1])

  elif op[0] == 'solved':
    check[int(op[1])] = 0 # solved한 후 0으로 바꾼 후 solved되었다고 표시

    while max_heap and check[-max_heap[0][1]] == 0: # solved한 값을 heap에서 바로 제거
      heapq.heappop(max_heap)
    while min_heap and check[min_heap[0][1]] == 0: # solved한 값을 heap에서 바로 제거
      heapq.heappop(min_heap)
