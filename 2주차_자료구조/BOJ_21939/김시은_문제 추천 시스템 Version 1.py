import sys; input = sys.stdin.readline 
from heapq import heappush, heappop

n = int(input())
heap = []
max_heap = []
p_check = {} # 현재 난이도 추적, 힙에 같은 문제번호 & 새로운 난이도로 들어올 수 있으니
for _ in range(n):
    p, l = map(int, input().split())
    heappush(heap, (l, p))
    heappush(max_heap, (-l, -p)) # 
    p_check[p] = True

m = int(input())
for _ in range(m):
    op, *args = input().split()
    if op[0] == 'a':
        p, l = map(int, args)
        # 같은 번호+다른 난이도 삽입되는 경우, 난이도 업데이트
        while not p_check[heap[0][1]]:
            heappop(heap)
        while not p_check[-max_heap[0][1]]:
            heappop(max_heap)
        p_check[p] = True
        heappush(heap, (l, p))
        heappush(max_heap, (-l, -p))

    elif op[0] == 's':
        p = int(args[0])
        p_check[p] = False
    
    elif op[0] == 'r':
        x = int(args[0])
        if x == 1: # max level
            while not p_check[-max_heap[0][1]]:
                heappop(max_heap) # op[0] == 's'에서 직접 pop하지 않았던 거 여기서 함
            print(-max_heap[0][1])
        else: # min level
            while not p_check[heap[0][1]]:
                heappop(heap)
            print(heap[0][1])