d = int(input())
s = 0
while d != 0:
    if d>=5:
        d = d - 5
    elif d>=4:
        d = d - 4
    elif d>=3:
        d = d - 3
    elif d>=2:
        d = d - 2
    elif d>=1:
        d = d - 1
    s += 1
print(s)