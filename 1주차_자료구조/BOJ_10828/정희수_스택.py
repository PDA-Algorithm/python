import sys
n = int(sys.stdin.readline())

strarr = []

for _ in range(n):
    arr = list(sys.stdin.readline().split())

    if arr[0] == 'push':
        strarr.append(int(arr[1]))
    
    elif arr[0] == 'pop':
        if len(strarr) == 0:
            print(-1)
        else:
            temp = strarr[-1]
            strarr.pop()
            print(temp) 
    
    elif arr[0] == 'size':
        print(len(strarr))
    
    elif arr[0] == 'empty':
        if len(strarr) == 0:
            print(1)
        else:
            print(0)
    
    elif arr[0] == 'top':
        if len(strarr) == 0:
            print(-1)
        else:
            print(strarr[-1])
