import sys
input = sys.stdin.readline

n = int(input())
total = 0

for _ in range(n):
    word = input().rstrip() #
    stack = []

    for i in word:
        if len(stack) == 0:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)

    if len(stack) == 0:
        total += 1

print(total)