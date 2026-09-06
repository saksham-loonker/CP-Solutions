t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    large = 10**18
    dp = [large] * (n + 1)
    for i in range(1, n + 1):
        if i <= k:
            dp[i] = int(s[i - 1])
        else:
            p = (i - 1) // k - 1
            best = large
            for j in range((p + 1) * k, p * k, -1):
                best = min(best, dp[j])
            dp[i] = int(s[i - 1]) + best
    ans = min(dp[n-k + 1:n + 1])
    print(ans)