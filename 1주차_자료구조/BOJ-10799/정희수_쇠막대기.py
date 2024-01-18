string = input()

# string = '()(((()())(())()))(())'

ans = 0

arr = []
for i in range(len(string)):
    if string[i] == '(':
        arr.append(string[i])
    elif string[i] == ')':
        if string[i-1] == '(':
            arr.pop()
            ans += len(arr)
        elif string[i-1] == ')':
            arr.pop()
            ans += 1


print(ans)