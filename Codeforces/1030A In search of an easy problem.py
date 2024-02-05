n = int(input())
p = list(map(int,input().split()))
f = True
for e in p:
    if e == 1:
        print('HARD')
        f = False
        break
if f:
    print('EASY')