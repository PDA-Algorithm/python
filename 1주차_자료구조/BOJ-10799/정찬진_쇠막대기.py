import sys

line = input()
stack = []
cnt = 0
for i in range(len(line)):
    if line[i] == "(":
        stack.append("(")
    else:
        if line[i - 1] == "(":
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1
print(cnt)