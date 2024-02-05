n = int(input())
l = []
for i in range(n):
    l.append(tuple(map(int,input().split())))

c = 0
for e in l:
    if e[1]-e[0]>=2:
        c += 1
print(c)