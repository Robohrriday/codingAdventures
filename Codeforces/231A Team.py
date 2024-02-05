n = int(input())
i = 0
j = 0
while i<n:
    l = list(map(int,input().split()))
    if l.count(1) >=2:
        j += 1
    i+=1
print(j)