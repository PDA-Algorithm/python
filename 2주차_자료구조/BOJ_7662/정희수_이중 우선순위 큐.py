'''
1. min_heap, max_heap 두개 사용
2. dict로 두개 힙 값 유무 동기화
'''

import heapq as hq
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())

    dict = {}
    min_heap = []
    max_heap = []

    for _ in range(k):
        msg = input().split()
        opt = msg[0]

        if opt == 'I':
            val = int(msg[1])
            hq.heappush(min_heap, val)
            hq.heappush(max_heap, -val)
            # dict[val] = dict.get(val, 0) + 1
            if dict.get(val) == None:
                dict[val] = 1
            else:
                dict[val] += 1
        
        elif opt == 'D':
            if len(dict) == 0:
                continue

            val = int(msg[1])
            # 최댓값 삭제
            if val == 1:
                while True:
                    delVal = hq.heappop(max_heap)
                    # 시간 초과난 부분
                    # if dict.get(-delVal) != None and dict.get(-delVal) >= 1:
                    # dict.get(val) 두번 조회하는 것보다, 
                    # dict.get(val) 한번만 조회하고 dict[val] 접근 한번하는게 시간 더 적게 소요
                    if dict.get(-delVal) != None and dict[-delVal] >= 1:
                        dict[-delVal] -= 1
                        if dict[-delVal] == 0:
                            del dict[-delVal]
                        break
            # 최솟값 삭제
            elif val == -1:
                while True:
                    delVal = hq.heappop(min_heap)
                    # if dict.get(delVal) != None and dict.get(delVal) >= 1:
                    if dict.get(delVal) != None and dict[delVal] >= 1:
                        dict[delVal] -= 1
                        if dict[delVal] == 0:
                            del dict[delVal]
                        break

    if len(dict) == 0:
        print('EMPTY')
    else:
        print(max(dict.keys()), min(dict.keys()))
