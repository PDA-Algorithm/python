import sys
input = sys.stdin.readline

p = input().rstrip()
stack = []
tmp = 1
res = 0

'''
1) 열린 괄호의 경우
 i) tmp(임시변수) 2 or 3 곱해주기
 ii) 스택에 Push

2) 닫힌 괄호의 경우
 i) 체크 (스택 길이 0 아닌지, 전 요소랑 짝이 맞는지) -> 아니면 바로 break
 ii) tmp값 결과에 더해주기
 iii) tmp값 2 or 3으로 나눠주기 (초기 값으로 컴백)
 iv) 스택 pop
'''

for i in range(len(p)):
    # 1. 열린 괄호
    if p[i] == '(':
        stack.append(p[i])
        tmp *= 2
    elif p[i] == '[':
        stack.append(p[i])
        tmp *= 3

    # 2. 닫힌 괄호
    elif p[i] == ')':
        if len(stack) == 0 or stack[-1] != '(':
            res = 0
            break
        if p[i-1] == '(':
            res += tmp #
        stack.pop()
        tmp //= 2
    elif p[i] == ']':
        if len(stack) == 0 or stack[-1] != '[':
            res = 0
            break
        if p[i-1] == '[':
            res += tmp
        stack.pop()
        tmp //= 3

if stack: # 남아 있으면
    res = 0
print(res)