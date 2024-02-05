n = int(input())
arr = list(map(int,input().split()))


def partition(arr,low,high):
	p = arr[low]
	i = low+1
	j = high
	
	while i < j:
		while i < j and arr[i] < p:
			i += 1
		while i < j and arr[j] > p :
			j -= 1
		if i == j:
			break
		else:
			arr[i],arr[j] = arr[j],arr[i]
			i += 1
			j -= 1
	if i == low+1:
		if arr[i] < p :
			arr[i],arr[low] = arr[low],arr[i]
			return i
		else:
			return low 
	elif i == high:
		if arr[i] < p :
			arr[i],arr[low] = arr[low],arr[i]
			return i
		else:
			arr[i-1],arr[low] = arr[low],arr[i-1]
			return i-1
	else:
		if arr[i] < p:
			arr[i],arr[low] = arr[low],arr[i]
			return i
		else:
			arr[i-1],arr[low] = arr[low],arr[i-1]
			return i-1

def quicksort(arr,n,low,high):
	if n == 1:
		return
	pi = partition(arr,low,high)
	if pi == low:
		quicksort(arr,high-pi,pi+1,high)
		return
	elif pi == high:
		quicksort(arr,pi-low,low,pi-1)
		return
	else:
		quicksort(arr,high-pi,pi+1,high)
		quicksort(arr,pi-low,low,pi-1)
		return

quicksort(arr,n,0,n-1)
print(arr)
		
	
			
			
		
	
	
				