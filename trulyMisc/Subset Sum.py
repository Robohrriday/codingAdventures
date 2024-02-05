def gcd(a,b):
    # a>b
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

n = int(input())
a = list(map(int,input().split()))
lcm = 0
for i in range(n-1):
    lcm = a[0]*a[1]//(gcd(a[0],a[1]))
    temp = a.pop(0)
    a[0] = lcm
print(a[0])