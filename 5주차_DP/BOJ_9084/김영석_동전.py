for tc in range(int(input())):
    N = int(input())
    coin = list(map(int, input().split()))
    M = int(input())
    dp = [0] * (M + 1)
    dp[0] = 1
    for i in range(N):  # 모든 동전에 대해 실행
        val = coin[i]
        for j in range(M + 1 - val):  # 0 부터 M-coin[i] 원에 대해 실행
            dp[j + val] += dp[j]
    print(dp[M])
