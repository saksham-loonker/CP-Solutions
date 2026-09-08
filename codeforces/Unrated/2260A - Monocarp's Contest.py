t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if a.count(0) < 2:
        print(-1)
        continue
    if a[0] == a[-1] == 0:
        print(0)
    elif a[0] == 1 and a[-1] == 1:
        print(2)
    else:
        print(1)