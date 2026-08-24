t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    v = sorted([a, b, c])
    rounds = 0
    while v[0] != v[1] and v[1] != v[2]:
        v[0] += 1   
        v[2] -= 1   
        v.sort()
        rounds += 1
    print(rounds)