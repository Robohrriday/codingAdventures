k,n,w = tuple(map(int, input().split()))
t = ((w*(w+1))//2)*k
if (t-n)>0:
    print(t-n)
else:
    print(0)