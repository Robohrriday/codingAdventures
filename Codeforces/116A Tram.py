n = int(input())
l = []
for i in range(n):
    l.append(tuple(map(int,input().split())))
t = 0
m = t
for e in l:
    t = t - e[0] + e[1]
    if t>=m:
        m = t
print(m)


