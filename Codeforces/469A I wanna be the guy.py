n = int(input())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
l = []
for i in x:
    if i not in l:
        l.append(i)
for i in y:
    if i not in l:
        l.append(i)
if 0 in l:
    l.remove(0)

if len(l) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")