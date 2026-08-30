t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    available = set()

    for _ in range(n):
        word = input()
        available.add(word[0].upper())

    possible = True

    for _ in range(m):
        abbr = input()

        if any(c not in available for c in abbr):
            possible = False

    print("YES" if possible else "NO")
