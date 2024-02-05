n = int(input())
arr = list(map(int,input().split()))


def partition(arr,n,low,high):
	p = arr[low]
	i = low+1
	j = high
	while i < j:
		while i < j and arr[i] < p:
			i +=1
		while i < j and arr[j] > p:
			j -= 1
		if i == j:
			break
		else:
			arr[i],arr[j] = arr[j],arr[i]
			i += 1
			j -= 1
	if i == low + 1:
		if arr[i] < p:
			arr[low],arr[i] = arr[i],arr[low]
		return
	elif i == high:
		if arr[i] < p:
			arr[i],arr[low] = arr[low],arr[i]
		else:
			arr[i-1],arr[low] = arr[low],arr[i-1]
		return
	else:
		if arr[i] < p:
			arr[i],arr[low] = arr[low],arr[i]
		else:
			arr[i-1],arr[low] = arr[low],arr[i-1]
		return

partition(arr,n,0,n-1)
print(arr)
			