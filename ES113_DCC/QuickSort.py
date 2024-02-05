a = [4,5,3,6,9,8,1,2,7]
n = 9

def quicksort(a,h,l):
    if len(a) == 1:
        return a
    x = []
    y = []
    p = a[0]

    for i in range(l,h+1):
        if p > a[i]:
            x.append(a[i])
        elif p < a[i]:
            y.append(a[i])

    print(x+[p]+y)

    quicksort(x,l+len(x)-1,l)
    quicksort(y,h,l+len(x)+1)

print(quicksort(a,n-1,0))