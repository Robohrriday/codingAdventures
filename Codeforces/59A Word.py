w = input()
l = 0
for e in w:
    if e.islower():
        l+=1
u = len(w)-l
if u>l:
    print(w.upper())
else:
    print(w.lower())
