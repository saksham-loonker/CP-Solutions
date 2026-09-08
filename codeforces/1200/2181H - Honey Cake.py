w, h, d = map(int, input().split())
n = int(input())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a = gcd(w, n)
n //= a

b = gcd(h, n)
n //= b

c = gcd(d, n)
n //= c

if n != 1:
    print(-1)
else:
    print(a-1, b-1, c-1)