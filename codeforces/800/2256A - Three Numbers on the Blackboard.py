t = int(input())
def replacemin(x,y,z,w):
    larg = w
    if x == larg:
        x=y+z
    elif y == larg:
        y=x+z
    else:
        z=x+y
    return x,y,z
for _ in range(t):
    a, b, c = map(int, input().split())
    temp1 = max(a,b,c)-min(a,b,c)
    a, b, c = replacemin(a,b,c,max(a,b,c))
    temp2 = max(a,b,c)-min(a,b,c)
    if temp2>temp1:
        print(temp1)
    else:
        print(temp2)
