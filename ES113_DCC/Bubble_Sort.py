n = int(input())
arr = list(map(int,input().split()))
j = 0 
while j < n-1:
	i = 0
	while i < n-1:
		if arr[i] < arr[i+1]:
			i += 1
		else:
			arr[i],arr[i+1] = arr[i+1],arr[i]
			i += 1
	j += 1
print(arr)


				