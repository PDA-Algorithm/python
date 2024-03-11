n, k = map(int, input().split())
num = list(map(int, input()))
stack = []

for x in num:
    while k > 0 and stack and stack[-1] < x:
        stack.pop()
        k -= 1
    stack.append(x)

# 만일 아직 삭제할 횟수(k)가 남아있다면, 남은 횟수만큼 뒤에서부터 삭제합니다.
if k > 0:
    stack = stack[:-k]

print("".join(map(str, stack)))
