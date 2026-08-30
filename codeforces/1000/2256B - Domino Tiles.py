MOD = 998244353

t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()
    ans = 1
    for start_index in [0, 1]:
        ways = 0
        for first in [0, 1]:
            valid = True
            expected = first

            for i in range(start_index, n, 2):
                if s[i] != '?' and int(s[i]) != expected:
                    valid = False
                    break

                expected ^= 1  # flip 0 <-> 1

            if valid:
                ways += 1

        ans = ans * ways % MOD

    print(ans)
