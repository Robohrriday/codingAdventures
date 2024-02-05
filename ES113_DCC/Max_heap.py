n = int(input())
arr = list(map(int,input().split()))

def shiftdown(arr,n,i):
	lc = 2*i+1
	rc = 2*i+2
	if rc < n and lc < n and arr[i] > arr[lc] and arr[i] > arr[rc]:
		return
	elif rc < n:
		if arr[lc] > arr[rc]:
			if arr[i] < arr[lc]:
				arr[i],arr[lc] = arr[lc],arr[i]
				shiftdown(arr,n,lc)
			return
		else:
			if arr[i] < arr[rc]:
				arr[i],arr[rc] = arr[rc],arr[i]
				shiftdown(arr,n,rc)
			return
	elif lc < n:
		if arr[lc] > arr[i]:
			arr[i],arr[lc] = arr[lc],arr[i]
			return
	else:
		return

def makeheap(arr,n,i):
	if n == 1:
		return
	lc = 2*i+1
	rc = 2*i+2
	if rc < n:
		makeheap(arr,n,rc)
		makeheap(arr,n,lc)
		shiftdown(arr,n,i)
		return
	elif lc < n:
		makeheap(arr,n,lc)
		shiftdown(arr,n,i)
		return
	else:
		return
makeheap(arr,n,0)
print(arr)

		
	
	
