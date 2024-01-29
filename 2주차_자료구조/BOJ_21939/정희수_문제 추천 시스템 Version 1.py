"""
mim_heap (L,P)
max_heap (-L,-P)
dict 로 min_heap, max_heap 동기화
"""

import sys
import heapq as hq
from collections import defaultdict

n = int(input())
min_heap = []
max_heap = []
dict = defaultdict(bool)

for _ in range(n):
    p, l = map(int, input().split())
    hq.heappush(min_heap, [l, p]) # x = -1 경우
    hq.heappush(max_heap, [-l, -p]) # x = 1 경우
    dict[p] = True

m = int(input())
for _ in range(m):
    str = input().split()
    cmd = str[0]

    if cmd == 'recommend':
        x = int(str[1])
        if x == -1:
            while True:
                if dict[min_heap[0][1]]: # 가장 쉬운 문제 있으면
                    print(min_heap[0][1]) # 문제 번호 출력
                    break
                hq.heappop(min_heap)
        elif x == 1:
            while True:
                if dict[-max_heap[0][1]]:
                    print(-max_heap[0][1])
                    break
                hq.heappop(max_heap)

    elif cmd == 'solved':
        p = int(str[1])
        dict[p] = False
    
    elif cmd == 'add':
        p, l = map(int, str[1:])

        # 추천 문제 리스트에 없는 문제 번호 p만 입력으로 주어짐
        # min_heap, max_heap에서 추출한 값이 dict에서 True인 값이 될 때까지 계속해서 pop
        # 시간 초과
        while not dict[min_heap[0][1]]:
            hq.heappop(min_heap)
        while not dict[-max_heap[0][1]]:
            hq.heappop(max_heap)
            
        dict[p] = True
        hq.heappush(min_heap, [l, p])
        hq.heappush(max_heap, [-l, -p])
