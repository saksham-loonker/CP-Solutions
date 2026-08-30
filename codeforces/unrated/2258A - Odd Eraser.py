from math import gcd

tcases = int(input())

for _ in range(tcases):
    n = int(input())
    a = list(map(int, input().split()))

    print(gcd(a[0], a[-1]))
