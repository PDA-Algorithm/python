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
        # 앞에 짝이 맞는 경우, result에 값 담아두기
        elif string[i-1] == '(':
            result += tmp
        tmp //= 2
        stack.pop()
    else:
        # stack에 남아있는게 없거나, 다른 짝일 경우
        if not stack or stack[-1] == '(':
            result = 0
            break
        # 앞에 짝이 맞는 경우, result에 값 담아두기
        elif string[i-1] == '[':
            result += tmp
        tmp //= 3
        stack.pop()

if stack:
    result = 0
print(result)
