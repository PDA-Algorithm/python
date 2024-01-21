import sys
input = sys.stdin.readline
s = []
for _ in range(int(input())):
    command = input().split()
    
    # push
    if len(command) != 1:
        s.append(command[-1])
    
    # pop
    elif command[0] == 'pop':
        if s:
            print(s.pop())
        else:
            print(-1)
            
    # size
    elif command[0] == 'size':
        print(len(s))
        
    # empty
    elif command[0] == 'empty':
        print(1 if not s else 0)
        
    # top
    else:
       print(s[-1] if s else -1)