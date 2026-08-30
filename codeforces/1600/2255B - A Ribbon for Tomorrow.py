MOD = 998244353
N = 10**6 + 5
t = int(input())

dp = [1] * N
for i in range(2, N):
    dp[i] = MOD - MOD // i * dp[MOD % i] % MOD

def C(ch,c):
    c = min(c, ch-c)
    ans = 1
    for i in range(1,c + 1):
        ans = ans * (ch - c + i) % MOD
        ans = ans * dp[i] % MOD
    return ans

for _ in range(t):
    n = int(input())
    s = input()

    ch = 0
    c = [0, 0]

    for i in range(n - 1):
        s1 = s[i] != s[i + 1]
        if s1:
            ch += 1
        else:
            c[ch % 2] += 1

    ans = C(c[0] + ch // 2, ch // 2)

    if ch:
        ans = ans * C(c[1] + (ch - 1) // 2, (ch - 1) // 2) % MOD

    print(ans)