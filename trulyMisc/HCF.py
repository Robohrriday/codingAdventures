total = int(input("Enter the total number of numbers whose HCF is to be found: "))

def start():
    n = int(input("Enter the number: "))
    return n 
firstnum = start()

firstset = set()
def factors(num,p):
    for j in range(1,num+1):
        if num % j == 0: 
            p.add(j)
            p.add(num)
    return p
s = factors(firstnum,firstset)

intersectionset = firstset
for k in range(0,total-1):
    tset = set()
    tnum = start()
    tset = factors(tnum,tset)
    intersectionset = intersectionset.intersection(tset)
intersectionlist = list(intersectionset)
intersectionlist.sort()
print(f"The HCF of the given numbers is: {intersectionlist[-1]}")