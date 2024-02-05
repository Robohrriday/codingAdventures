n = int(input("Enter the number of elements in the set: "))
l = []
for i in range(0,n):
    a = int(input(f"Enter the element ({i+1}): "))
    l.append([a])

l_actual = l.copy()
l_temp = l.copy()

while len(l_temp) != len(l_actual)**len(l_actual):
    temp_list = []
    temp_list.clear()
    for o_l_actual in l_actual:
        for o_l_temp in l_temp:
            o_l_temp.sort()
            if o_l_actual[0] in o_l_temp:
                temp_list.append(o_l_temp)
            else:
                union_element = o_l_actual + o_l_temp
                union_element.sort()
                temp_list.append(union_element)
    l_temp = temp_list.copy()

final =[]
for item in l_temp:
    if item in final:
        pass
    else:
        final.append(item)
final.append(None)
print(final)
