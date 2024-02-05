def grid_Permutations(l):
    a = []
    for i in l:
        for j in l:
            for k in l:
                a.append([i,j,k])
    return a

def point_Permutations(l):
    a = []
    for i in l:
        m = l.copy()
        m.remove(i)
        for j in m:
            n = m.copy()
            n.remove(j)
            for k in n:
                a.append([i,j,k])
    pc = []
    for e in a:
        if e not in pc:
            pc.append(e)
    return pc
