n = int(input())
l = []

def Merge(arr1,arr2,n1,n2):
	i = 0
	j = 0
	arr3 = []
	while i < n1 and j < n2:
		if arr1[i] < arr2[j]:
			arr3.append(arr1[i])
			i += 1
		elif arr1[i] > arr2[j]:
			arr3.append(arr2[j])
			j += 1
		else:
			arr3.append(arr1[i])
			i += 1
			j += 1
	while i < n1:
		arr3.append(arr1[i])
		i += 1
	while j < n2:
		arr3.append(arr2[j])
		j += 1
	return arr3


for i in range(n):
	l.append(list(map(int,input()[1:-1].split(','))))

for i in range(n):
	l[i] = list(range(l[i][0],l[i][1]+1))
arr = l[0]
for i in range(1,n):
	arr = Merge(arr,l[i], len(arr),len(l[i]))
print(arr)
	

				