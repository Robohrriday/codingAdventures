def factorial(num):
    a = 1
    for i in range (1,num+1):
        a = a * i
    return a
    
n = int(input("Enter the number of rows: "))

print(" " * (n-1),end="")
print("1",end="")
print(" " * (n-1))

print(" " * (n-2),end="")
print("1 1",end="")
print(" " * (n-2))

for i in range (2, n):
    print(" " * (n-1-i),end="")
    for j in range (0,i+1):
        f = int(factorial(i)/(factorial(i-j)*factorial(j)))
        if j == i:
            print(str(f) + " ")
        else:
            print(str(f) + " ",end="")