def merger(l1,l2):
    s = []
    p1 = 0
    p2 = 0
    while p1<len(l1) and p2<len(l2):
        if l1[p1]>l2[p2]:
            s.append(l2[p2])
            p2 = p2 + 1
        else:
            s.append(l1[p1])
            p1 = p1 + 1
    if p1<len(l1):
        s += l1[p1:]
    if p2<len(l2):
        s += l2[p2:]
    return s

print(merger([2,4,6,8],[1,3,5,7]))