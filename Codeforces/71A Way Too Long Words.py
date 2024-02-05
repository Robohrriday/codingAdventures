n = int(input())
i = 0
while i<n:
    a = input()
    l = len(a)
    if l<=10:
        print(a)
    else:
        print(a[0] + str(l-2) + a[-1])
    i += 1
