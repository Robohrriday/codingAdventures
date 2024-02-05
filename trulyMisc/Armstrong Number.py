for k in range(0, 10000):
    num = str(k)
    l = []
    for i in range(0, len(num)):
        l.insert(i,num[i])
    s = 0
    for j in range(0,len(num)):
        s = s + ((int(l[j])) ** len(num))
    if int(num) == s:
        print(f"{num} ", end="")
    else:
        pass
