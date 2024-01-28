import sys
import heapq
from collections import defaultdict

# max_q, min_q에 있는 정수가 진짜 있는 정수인지 존재 여부 확인 필요!!!!!!!!!!

"""
정수 최초삽입/중복삽입 경우의 수 나눠서 
중복 삽입일 경우에는 heappush 안하고 check[n] += 1,
최초 삽입일 경우에는 heappush와 check[n] = 1 처리 해주었더니

입력)
I 2
D 1
I 2

이 입력의 경우,
마지막 출력 while 문에서 max_q에 아무것도 없는데 출력하려고 해서 IndexError 발생
=> defaultdict 사용해서 딕셔너리 초기화,
모든 정수 삽입에 heappush와 check[n] += 1 처리
"""

T = int(sys.stdin.readline())

for i in range(T):
  k = int(sys.stdin.readline())
  num = 0
  max_q = []
  min_q = []
  check = defaultdict(int) # 실제 존재 여부 확인, 0으로 딕셔너리 초기화
  for i in range(k):
    order, n = sys.stdin.readline().rstrip().split()
    n = int(n)
    if order == "I":
      check[n] += 1
      heapq.heappush(max_q, -n)
      heapq.heappush(min_q, n)
      num += 1 # 큐 길이 +1
    elif order == "D":
      if num > 0:
        if n == 1:
          while True:
            del_num = -heapq.heappop(max_q) # 힙에서 정수 제거
            if check[del_num] != 0: # 존재 여부 1 이상이라면 
              check[del_num] -= 1 # 존재 여부 0으로 만들어주고 break
              break
        else:
          while True:
            del_num = heapq.heappop(min_q)
            if check[del_num] != 0:
              check[del_num] -= 1
              break
        num -= 1 # 큐 길이 -1
  if num > 0:
    while True:
      max_del = -heapq.heappop(max_q)
      if check[max_del] != 0 :
        break
    while True:
      min_del = heapq.heappop(min_q)
      if check[min_del] != 0 :
        break
    print(max_del, min_del)
  else:
    print("EMPTY")


