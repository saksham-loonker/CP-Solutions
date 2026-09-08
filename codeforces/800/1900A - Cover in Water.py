t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(str, input()))

    fin = 0

    for i in range(n):
        if i + 2 < n and s[i] == '.' and s[i + 1] == '.' and s[i + 2] == '.':
            fin = 2
            break
        if s[i] == '.':
            fin += 1
    print(fin)