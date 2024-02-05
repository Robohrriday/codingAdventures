n = int(input())
arr = list(map(int,input().split()))
i = 0

while i < n-1:
	if arr[i] < arr[i+1]:
		i += 1
		continue
	else:
		if i == 0 and arr[i] > arr[i+1]:
			arr[i],arr[i+1] = arr[i+1],arr[i]
			i += 1
			continue
		j = i
		k = arr[i+1]
		while j > 0:
			if k < arr[j]:
				arr[j],arr[j+1] = arr[j+1],arr[j]
				j -= 1
			else:
				break
		if j == 0 and arr[j] > k:
			arr[1],arr[0] = arr[0],arr[1]
		i += 1

print(arr)

				