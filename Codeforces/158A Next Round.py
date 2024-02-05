n,k = tuple(map(int,input().split()))
l = list(map(int,input().split()))
j = 0
for i in l:
    if i>0 and i>=l[k-1]:
        j += 1
print(j)