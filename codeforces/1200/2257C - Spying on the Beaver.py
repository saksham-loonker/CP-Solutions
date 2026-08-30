tcases = int(input())

for _ in range(tcases):
    n = int(input())
    parents = list(map(int, input().split()))

    m = int(input())
    dams = list(map(int, input().split()))

    skip = min(dams)

    cameras = []

    for dam in dams:
        if dam != skip:
            cameras.append(dam)

    print(len(cameras), *cameras)
