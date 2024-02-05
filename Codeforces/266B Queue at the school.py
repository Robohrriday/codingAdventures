n,t = tuple(map(int,input().split()))
p = list(input())
while t!=0:
    i = 0
    while i<n-1:
        if p[i] + p[i+1] == "BG":
            p[i],p[i+1] = p[i+1],p[i]
            i += 2
        else:
            i += 1
    t = t - 1
print(*p,sep='')