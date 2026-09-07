t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    zeros = []

    for i in range(n):
        if a[i] == 0:
            zeros.append(i)

    if len(zeros) == 1:
        print("NO")
    else:
        print("YES")

        ans = ["C"] * n

        if len(zeros) >= 2:
            ans[zeros[0]] = "A"

            for i in range(1, len(zeros)):
                ans[zeros[i]] = "B"

        print("".join(ans))