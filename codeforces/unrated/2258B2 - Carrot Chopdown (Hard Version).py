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
    answer= []
    cur = f[:]
    p = 2
    while p <= m:
        half = p//2
        ans = answer[-1] if answer else 0
        for x in range(1, m//half+1):
            now = cur[x] - f[half*x]
            limit = min(m // x, p-1)
            now += sum(s[half*x:(limit + 1) * x:x])
            if p*x <= m:
                now += f[p*x]
            cur[x] = now
            ans = max(ans, now)
        answer.append(ans)
        p = p*2
    total = sum(a)

    while len(answer) < m:
        answer.append(total)

    print(' '.join(map(str, answer)))
