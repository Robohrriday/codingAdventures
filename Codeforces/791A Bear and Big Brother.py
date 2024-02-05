l,b= tuple(map(int,input().split()))
c = 0
while l <= b:
    l *= 3
    b *= 2
    c = c + 1
print(c)