t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    copy_a = [0] + a + [x]
    large = 0
    for i in range(1, len(copy_a)):
        if i == len(copy_a) - 1:
            large = max(large, 2 * (copy_a[i] - copy_a[i - 1]))
        else:
            large = max(large, copy_a[i] - copy_a[i - 1])
    print(large)