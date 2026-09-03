t = int(input())

for _ in range(t):
    n = int(input())
    a  = list(map(int,input().split()))
    c = []
    s  = []
    for x in a:
        if not c or c[-1] != x:
            c.append(x)
            s.append(1)
        else:
            s[-1] += 1
    m = len(c)
    ans= m
    good = False
    for i in range(m-1):
        if s[i] > 1 and s[i+1] > 1:
            ans = m + 2
            good = True
            break
    if not good:
        for i in range(m-1):
            if s[i] > 1:
                if i+2 >= m or c[i] != c[i+2]:
                    ans = m + 1
                    break

            if s[i+1] > 1:
                if i == 0 or c[i+1] != c[i-1]:
                    ans = m + 1
                    break

    print(ans)