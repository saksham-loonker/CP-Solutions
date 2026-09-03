import math
t = int(input())
def count_steps(l, r):
    if r - l == 1:
        return 0
    mid = (l + r) // 2
    left = count_steps(l, mid)
    right = count_steps(mid, r)
    if left == -1 or right == -1:
        return -1
    value = 0
    maxofl = max(p[l:mid])
    minofl = min(p[l:mid])
    maxofr = max(p[mid:r])
    minofr = min(p[mid:r])
    if maxofl < minofr:
        value = 0
    elif maxofr < minofl:
        value = 1
    else:
        return -1
    return left + right + value

for _ in range(t):
    m = int(input())
    p = list(map(int, input().split()))
    print(count_steps(0, m))
