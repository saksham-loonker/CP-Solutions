tcases = int(input())
for _ in range(tcases):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    f = [0] * (m+2)
    for x in a:
        f[x] +=1
    s = [0]* (m+2)
    for i in range(m, 0, -1):
        s[i] = s[i+1] + f[i]
    ans=0
    for x in range(1, m+1):
        now = f[x] + s[x+1]
        if x*2 <= m:
            now += f[x*2]
        ans = max(ans, now)
    print(ans)
