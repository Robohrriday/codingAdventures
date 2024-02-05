n = int(input())
p = list(map(int,input().split()))

f = []
for i in range(n):
    f.append(0)

for e in p:
    f[e-1] = p.index(e) + 1
print(*f)