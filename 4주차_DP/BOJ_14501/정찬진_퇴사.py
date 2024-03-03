import sys
n = int(sys.stdin.readline())
time = [0]
pay = [0]
dp = [0] * (n+1)
for i in range(n):
  a,b = map(int,sys.stdin.readline().split())
  time.append(a)
  pay.append(b)

for i in range(1,n+1):
  if i + time[i]-1<=n:
    dp[i+time[i]-1] = max(dp[i+time[i]-1],dp[i-1]+pay[i],max(dp[0:i])+pay[i])
print(max(dp))
