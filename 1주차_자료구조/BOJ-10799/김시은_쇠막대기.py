import sys
input = sys.stdin.readline

x = input().rstrip()
stack = []
res = 0

for i in range(len(x)):
    if x[i] == '(':
        stack.append('(')
    else:
        stack.pop()
        if x[i - 1] == '(': # '()' 레이저인 경우
            res += len(stack)
        else: # ')' 막대의 끝인 경우
            res += 1

print(res)