n = int(input())
s = ''
for i in range(n):
    s = s + input()
b = 0
for j in range(2,len(s),2):
    if s[j] == s[j-1]:
        b += 1
print(b+1)