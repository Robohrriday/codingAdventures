a1 = [1,5,9,15,79,89,500]
a = [89,500,1,5,9,15,79]
#for i in range(len(a)-1):
#    if a[i]>a[i+1]:
#        break
#print(len(a)-i-1)
if len(a) == 2:
    print(1)
else:
    h = len(a)-1
    l = 0
    while True:
        m = (h+l)//2
        if a[m]>a[m+1] and a[m]>a[m-1]:
            break
        elif a[l]>a[m+1]:
            h = m
        else:
            l = m
    print(len(a)-m-1)
