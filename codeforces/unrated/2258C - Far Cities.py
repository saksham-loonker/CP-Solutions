tcases = int(input())

def ask(a, b, dist):
    print("?", a, b, dist, flush=True)
    return int(input())

for _ in range(tcases):
    n = int(input())

    u = 1
    v = 1
    d= 0

    for x in range(2, n+1):
        old_u = u
        old_v =v

        old_d = d

        while ask(x, old_u, d + 1):
            d +=1

        if d > old_d:
            u = x
            v = old_u
        
        before = d

        while ask(x, old_v, d+1):
            d += 1

        if d > before:
            u = x
            v = old_v

    print("!", u, v, d, flush=True)
