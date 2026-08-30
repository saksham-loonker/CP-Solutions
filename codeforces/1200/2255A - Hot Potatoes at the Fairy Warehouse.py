t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input()

    total = 2 * n
    red = 0
    blue = 0

    for i in range(total):
        if s[i] == '0':
            continue

        next_guy = (i + 1) % total

        if s[next_guy] == '0':
            if i % 2 == 0:
                red += 1
            else:
                blue += 1

        else:
            if i % 2 == 0:
                blue += 1
            else:
                red += 1

    print(red, blue)
