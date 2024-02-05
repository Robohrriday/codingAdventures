a = [1,10,70,2,4]

# Insertion Sort
for i in range(len(a)-1):
    if a[i+1]<a[i]:
        j = i+1
        while j>0:
            if a[j-1]>a[j]:
                a[j],a[j-1] = a[j-1],a[j]
            else:
                break
            j -= 1
print(a)

# Bubble Sort
for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        if a[j+1]<a[j]:
            a[j+1],a[j] = a[j],a[j+1]
print(a)
 