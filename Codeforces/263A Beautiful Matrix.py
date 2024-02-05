m = []
for t in range(5):
    t1 = list(map(int,input().split()))
    m.append(t1)

for x in range(5):
    f = True
    for y in range(5):
        if m[x][y] == 1:
            f = False
            break
    if not f:
        break
pl =  (x-2)**2 + (y-2)**2
c = 0
while pl != 0:
    if (x-1)**2 + (y-2)**2 < pl:
        pl = (x-1)**2 + (y-2)**2
        x = x + 1
    elif (x-3)**2 + (y-2)**2 < pl:
        pl = (x-3)**2 + (y-2)**2
        x = x - 1
    elif (x-2)**2 + (y-1)**2 < pl:
        pl = (x-2)**2 + (y-1)**2
        y = y + 1
    else:
        pl = (x-2)**2 + (y-3)**2
        y = y - 1
    c = c + 1
print(c)
