m0 = [63, 57]
m1 = [82, 66, 87, 78, 77, 92, 83]
m2 = [97, 53, 53, 85, 58, 54]
m3 = [50]
m4 = [64, 69, 52, 65, 73]
m5 = [57, 91, 65]
m6 = [67, 91, 84, 78, 60, 69, 99, 83]
m7 = [58, 78, 69, 65]
lm = [m0,m1,m2,m3,m4,m5,m6,m7]
tfl = [[m6,m2],[m5,m0],[m4,m3],[m1,m7],[m3,m7],[m0,m6],[m2,m4],[m5,m1]]
def f0(w,t,f):
    nw = w * 11
    if nw % 7 == 0:
        t.append(nw)
    else:
        f.append(nw)

def f1(w,t,f):
    nw = w + 1
    if nw % 11 == 0:
        t.append(nw)
    else:
        f.append(nw)

def f2(w,t,f):
    nw = w * 7
    if nw % 13 == 0:
        t.append(nw)
    else:
        f.append(nw)

def f3(w,t,f):
    nw = w + 3
    if nw % 3 == 0:
        t.append(nw)
    else:
        f.append(nw)

def f4(w,t,f):
    nw = w + 6
    if nw % 17 == 0:
        t.append(nw)
    else:
        f.append(nw)

def f5(w,t,f):
    nw = w + 5
    if nw % 2 == 0:
        t.append(nw)
    else:
        f.append(nw)

def f6(w,t,f):
    nw = w * w
    if nw % 5 == 0:
        t.append(nw)
    else:
        f.append(nw)

def f7(w,t,f):
    nw = w + 7
    if nw % 19 == 0:
        t.append(nw)
    else:
        f.append(nw)

d = [[f0,0],[f1,0],[f2,0],[f3,0],[f4,0],[f5,0],[f6,0],[f7,0]]

for i in range(10000):
    for j in range(8):
        for k in lm[j]:
            d[j][0](k,tfl[j][0],tfl[j][1])
        d[j][1] = d[j][1] + len(lm[j])
        lm[j].clear()

cnt  = []
for a in d:
    cnt.append(a[1])
cnt.sort()
print(cnt[-1]*cnt[-2])

# 