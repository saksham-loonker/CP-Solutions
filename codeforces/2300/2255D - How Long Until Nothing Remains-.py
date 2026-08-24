def can_finish(a, n, seconds):
    removed = max(0, seconds - 30)
    remaining = n - removed

    if remaining <= 0:
        return True

    b = a[:remaining]

    for bit in range(min(seconds, 30) - 1, -1, -1):
        if not b:
            return True

        power = 1 << bit

        if b[-1] <= power:
            b.pop()
        else:
            b[-1] -= power

            i = len(b) - 1
            while i > 0 and b[i] < b[i - 1]:
                b[i], b[i - 1] = b[i - 1], b[i]
                i -= 1

    return not b


t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    low = n
    high = n + 30

    while low < high:
        mid = (low + high) // 2

        if can_finish(a, n, mid):
            high = mid
        else:
            low = mid + 1

    print(low)