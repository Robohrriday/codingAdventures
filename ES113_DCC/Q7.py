def merge(a,b):
    if a[0]>b[-1]:
        print('1:True')
        return b+a
    elif a[-1]<b[0]:
        print('2:True')
        return a+b
    else:
        m = len(a)
        n = len(b)
        r = []
        i = 0
        j = 0
        if m>n:
            while j<n:
                if a[i]>b[j]:
                    r.append(b[j])
                    j+=1
                elif a[i]<b[j]:
                    r.append(a[i])
                    i+=1
                else:
                    r.append(a[i])
                    r.append(b[j])
                    i+=1
                    j+=1
            print('3:True')
            return r+a[i:]
        else:
            while i<m:
                if a[i]>b[j]:
                    r.append(b[j])
                    j+=1
                elif a[i]<b[j]:
                    r.append(a[i])
                    i+=1
                else:
                    r.append(a[i])
                    r.append(b[j])
                    i+=1
                    j+=1
            print('4:True')
            return r+b[j:]

lists = [[1,3,5,7,9],[2,4,6],[-1,0],[3,10,11,12]] # N = 14

m = lists[0]
for i in range(1,len(lists)):
    m = merge(m,lists[i])
    print(m)



