t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    oomo = []
    for index in range(n):
        if a[index] != 0:
            oomo.append(index)
    if len(oomo) > 0:
        best_len = -1
        best_lw = 0
        best_high = 0
        curr_lw = 0
        for r in range(len(oomo)):
            span = oomo[r] - oomo[curr_lw]
            if span > best_len:
                best_len = span
                best_lw = curr_lw
                best_high = r
            if a[oomo[r]] == 1:
                curr_lw = r
        a[oomo[best_lw]] = 1
        a[oomo[best_high]] = 1
    for i in range(n):
        if a[i] == -1:
            a[i] = 0
    output = []
    for i in range(n):
        output.append(str(a[i]))
    print(" ".join(output))