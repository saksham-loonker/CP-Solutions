t = int(input())

def calculate_distance(l, r, depth_of_max):
    if l>r:
        return
    m=l
    for j in range(l, r + 1):
        if a[j] > a[m]:
            m = j
    depths[m] = depth_of_max
    calculate_distance(l, m - 1, depth_of_max + 1)  
    calculate_distance(m + 1, r, depth_of_max + 1)  

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    depths = [0] * n
    calculate_distance(0, n - 1, 0)
    print(*depths)