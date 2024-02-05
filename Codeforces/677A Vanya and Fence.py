n,h = tuple(map(int,input().split()))
lh = list(map(int,input().split()))

w = 0
for i in range(n):
    if lh[i] > h:
        w += 2
    else:
        w += 1
print(w)
