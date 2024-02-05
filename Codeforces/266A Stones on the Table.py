n = int(input())
p = input()
c = 0
for i in range(n-1):
    if p[i]+p[i+1] in ['RR','BB','GG']:
        p = p[:i] + " " + p[i+1:]
        c = c + 1
print(c)