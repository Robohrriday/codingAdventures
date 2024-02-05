a = int(input())

def c(n):
    s = str(n)
    l = []
    for e in s:
        if e not in l:
            l.append(e)
    if len(s) == len(l):
        return True
    else:
        return False
p = a + 1
while True:
    if c(p):
        print(p)
        break
    else:
        p = p + 1
