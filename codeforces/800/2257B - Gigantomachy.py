cases = int(input())

for _ in range(cases):
    n, m = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    bea = 0
    ver = 0

    for i in range(n - 1):
        bea += a[i] - a[i + 1] + 1
    bea += a[-1]

    for i in range(m - 1):
        ver += b[i] - b[i + 1] + 1
    ver += b[-1]

    if bea >= ver:
        print(1)
    else:
        print(2)
