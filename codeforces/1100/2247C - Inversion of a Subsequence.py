t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if a == b:
        print(0)
        continue

    if sum(a) == 0 or sum(b) == n:
        print(-1)
        continue

    s = 0
    for i in range(n):
        if a[i] != b[i]:
            s = s + a[i]

    if s % 2 == 1:
        print(1)
    else:
        print(2)