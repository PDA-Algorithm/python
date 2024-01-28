'''
1. 최대힙과 최소힙을 두어, 현재 유효한 원소 개수를 count에 관리한다.
2. count가 0이 되기 전까지는 현재 최대 / 최소를 제외하고 heap 요소들을 신뢰할 수 없다.
3. 최소값을 삭제했다면 del_min_heap에 기록, 삭제된 최대값은 del_max_heap에 push
    count가 0이 되면 min_heap, max_heap, del_min_heap, del_max_heap을 전부 비운다.
4. 삭제시 반대쪽 삭제기록과 비교해 진짜 원소를 pop할때까지 계속 pop한다.
'''

import sys
input = sys.stdin.readline
import heapq

def Delete(From, Ref, To):
    global count
    while True:
        if not Ref or From[0] < Ref[0]:
            heapq.heappush(To, -heapq.heappop(From))
            count -= 1
            return
        else:
            heapq.heappop(From)
            heapq.heappop(Ref)


t = int(input())
for tc in range(t):
    
    # 저장된 데이터
    min_heap = []
    max_heap = []
    
    # 지운 데이터
    min_del_heap = []
    max_del_heap = []
    count = 0
    
    k = int(input())
    for _ in range(k):
        command, num = input().rstrip().split()
        
        if command == 'I':
            heapq.heappush(max_heap, -int(num))
            heapq.heappush(min_heap, int(num))
            count += 1
            
        elif count:
            if num == '1':
                Delete(max_heap, min_del_heap, max_del_heap)
                    
            else:
                Delete(min_heap, max_del_heap, min_del_heap)

            # heap이 비었을 경우 초기화
            if not count:
                min_heap = []
                max_heap = []
                min_del_heap = []
                max_del_heap = []
                
    if not count:
        print('EMPTY')
        continue

    while min_del_heap and max_heap[0] == min_del_heap[0]:
        heapq.heappop(max_heap)
        heapq.heappop(min_del_heap)

    while max_del_heap and min_heap[0] == max_del_heap[0]:
        heapq.heappop(min_heap)
        heapq.heappop(max_del_heap)
        
    print(-max_heap[0], min_heap[0])