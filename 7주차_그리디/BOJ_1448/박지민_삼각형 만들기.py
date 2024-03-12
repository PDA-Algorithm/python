# 1448
import sys
input = sys.stdin.readline

N = int(input())
answer = -1     # 삼각형을 만들 수 없을 경우 -1
lines = []

for _ in range(N):
    lines.append(int(input()))
lines = sorted(lines, reverse=True)

# 삼각형을 만들 수 있는 조합 (한 변의 길이보다 나머지 두 변의 합이 더 커야 함) 중
    # 세 변의 길이의 합 최대값
for i in range(N-2):
    if lines[i] < lines[i+1] + lines[i+2]:
        answer = lines[i] + lines[i+1] + lines[i+2]
        break

print(answer)
