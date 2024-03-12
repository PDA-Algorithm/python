# 2812
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
number = list(input().rstrip())  # rstrip()으로 \n 제거
stack = []

# 스택 이용 - 가장 최근에 들어온 값과 새로 들어온 값 비교 -> 새 값이 더 클 경우 스택 pop
for i in range(N):
    while K>0 and stack and stack[-1] < number[i]:
        stack.pop()
        K -= 1
    stack.append(number[i])

print(''.join(stack[:len(stack)-K]))    # for 문 다 돌았는데 k가 남아있을 경우
