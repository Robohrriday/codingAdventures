n = input()
c = 0
for e in n:
    if e == '4' or e =='7':
        c += 1

c = str(c)
f = True
for i in c:
    if i == '4' or i == '7':
        pass
    else:
        f = False
        print('NO')
        break
if f:
    print('YES')