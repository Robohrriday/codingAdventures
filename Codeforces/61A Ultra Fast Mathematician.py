a = input()
b = input()
s = ''
for i in range(len(a)):
    if a[i] == b[i]:
        s = s + '0'
    else:
        s = s + '1'
print(s)