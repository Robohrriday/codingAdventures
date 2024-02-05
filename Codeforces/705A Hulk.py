n = int(input())
s = ''
if n==1:
    s = 'I hate it'
else:
    for i in range(n):
        if i%2 == 0 and i != n-1:
            s = s + 'I hate that '
        elif i%2 == 0 and i == n-1:
            s = s + 'I hate it'
        elif i%2 == 1 and i != n-1:
            s = s + 'I love that '
        elif i%2 == 1 and i == n-1:
            s = s + 'I love it'
print(s)
    