total = int(input("Enter the number of numbers whose LCM is to found: "))

def factors(num):
    flist_of_factors = set()
    for c in range(1,num+1):
        if num % c == 0:
            flist_of_factors.add(c)
    return flist_of_factors


list_of_num = []
for a in range(0,total):
    temp_num = int(input(f"Enter the number {a+1}: "))
    list_of_num.append(temp_num)

for b in range (0,total-1):
    set0 = factors(list_of_num[0])
    set1 = factors(list_of_num[1])
    intersection_set = set0.intersection(set1)
    intersection_list = list(intersection_set)
    intersection_list.sort()
    lcm = int((list_of_num[0]*list_of_num[1])/intersection_list[-1])
    list_of_num.remove(list_of_num[1])
    list_of_num.remove(list_of_num[0])
    list_of_num.insert(0,lcm)
print(f"LCM of the given numbers is {list_of_num[0]}.")