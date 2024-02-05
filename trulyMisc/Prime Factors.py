opint = int(input("Enter the opening interval: "))
clint = int(input("Enter the closing interval: "))

def factors(num,s):
    for i in range(1,num+1):
        if num % i == 0:
            s.append(i)
    return s

prime_factors = []
for j in range(opint,clint+1):
    l = []
    l = factors(j,l)
    if len(l) == 2:
        prime_factors.append(j)
    else:
        pass
print(f"The prime factors in the given range are: {prime_factors}")
        
