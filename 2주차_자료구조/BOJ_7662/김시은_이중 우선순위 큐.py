import sys, heapq as hp
input = sys.stdin.readline

def priority_queue():
    k = int(input()) # 연산의 개수
    heap = []
    max_heap = []
    check = [True] * k

    for i in range(k):
        op, num = input().split()
        num = int(num)

        if op == 'I':
            hp.heappush(heap, (num, i))
            hp.heappush(max_heap, (-num, i))
        else:
            # 원소 제거 + check False로
            if num == 1 and max_heap: # 최댓값 삭제
                max_value = hp.heappop(max_heap)[1]
                check[max_value] = False
                # max_heap.remove((-max_value, max_value))

            elif num == -1 and heap: # 최솟값 삭제
                min_value = hp.heappop(heap)[1]
                check[min_value] = False
                # heap.remove((-min_value, min_value)) # 튜플을 삭제해야지

        # heap, max_heap 동일하게 맞춰주기
        while heap and check[heap[0][1]] == False: # 최소힙의 맨 위에 있는 원소(최솟값)의 check가 False면 이미 다른 쪽에서 지워진 경우이므로 해당 원소 제거
            hp.heappop(heap)
        while max_heap and check[max_heap[0][1]] == False:
            hp.heappop(max_heap)
        
    if heap:
        print(-max_heap[0][0], heap[0][0])
    else:
        print('EMPTY')


if __name__ == '__main__':
    for _ in range(int(input())):
        priority_queue()

# 최소 힙 - 힙의 맨 위에 있는 원소 - 최솟값
# 최대 힙 - 힙의 맨 위에 있는 원소 - 최댓값