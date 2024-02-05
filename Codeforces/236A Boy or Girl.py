a = list(input())
b = []
for e in a:
    if e not in b:
        b.append(e)
l = len(b)
if l%2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
