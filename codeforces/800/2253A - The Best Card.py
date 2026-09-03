def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    root = int(x **0.5) + 1
    for i in range(3, root, 2):
        if x % i == 0:
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    if is_prime(n+1):
        print("YES")
    else:
        print("NO")