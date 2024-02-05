n = int(input())
p = input()
d = 0
for e in p:
    if e == "D":
        d += 1
a = n-d
if a>d:
    print('Anton')
elif a==d:
    print('Friendship')
else:
    print('Danik')