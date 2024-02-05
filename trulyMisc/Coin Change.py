num = int(input("Enter the number: "))
n = int(input("Enter the number of distinct changes: "))

l = []
for i in range (0,n):
    a = int(input("Enter a change: "))
    l.append([a])
l.sort()

l_actual = l.copy()
l_temp = l.copy()
final = []
while len(l_temp) != len(l_actual)**len(l_actual):
    temp_list = []
    temp_list.clear()
    for o_l_actual in l_actual:
        for o_l_temp in l_temp:
            union_element = o_l_actual + o_l_temp
            temp_list.append(union_element)
    l_temp = temp_list.copy()
    for item in l_temp:
        if sum(item) == num:
            item.sort()
            final.append(item)
    else:
        pass
print(l_temp)
finalfinal = []
for item in final:
    if item not in finalfinal:
        finalfinal.append(item)
print(finalfinal)
