"""
1. (, [ -> tmp *= 2, tmp *= 3
2. ) -> tmp //= 2, 앞이 ( 면 res에 tmp 값 추가
3. ] -> tmp //= 3, 앞이 [ 면 res에 tmp 값 추가
"""

string = input()
stack = []
tmp = 1
result = 0

for i in range(len(string)):
    if string[i] == '(':
        tmp *= 2
        stack.append('(')
    elif string[i] == '[':
        tmp *= 3
        stack.append('[')
    elif string[i] == ')':
        # stack에 남아있는게 없거나, 다른 짝일 경우
        if not stack or stack[-1] == '[':
            result = 0
            break
        # 앞에 짝이 맞는 경우, result에 값 더하기
        elif string[i-1] == '(':
            result += tmp
        tmp //= 2
        stack.pop()
    else:
        # stack에 남아있는게 없거나, 다른 짝일 경우
        if not stack or stack[-1] == '(':
            result = 0
            break
        # 앞에 짝이 맞는 경우, result에 값 더하기
        elif string[i-1] == '[':
            result += tmp
        tmp //= 3
        stack.pop()

if stack:
    result = 0
print(result)
