t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    odd = 0
    cnt = [0, 0]
    for x in a:
        if x%2==1:
            odd += 1
        else:
            cnt[(x//2) % 2] += 1
    print(max(odd, cnt[0], cnt[1]))