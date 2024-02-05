b = [2,4,6]
a = [1,3,5,7,9]
r = []

if a[0]>b[-1]:
    print(b+a)
elif a[-1]<b[0]:
    print(a+b)
else:
    m = len(a)
    n = len(b)
    i = 0
    j = 0
    if m>n:
        while j < n:
            if a[i]>b[j]:
                r.append(b[j])
                j+=1
            elif a[i]<b[j]:
                r.append(a[i])
                i+=1
            else:
                r.append(a[i])
                r.append(b[j])
                i += 1
                j += 1
        print(r+a[i:])
    else:
        while i < m:
            if a[i]>b[j]:
                r.append(b[j])
                j+=1
            elif a[i]<b[j]:
                r.append(a[i])
                i+=1
            else:
                r.append(a[i])
                r.append(b[j])
                i += 1
                j += 1
        print(r+b[j:])     

if 