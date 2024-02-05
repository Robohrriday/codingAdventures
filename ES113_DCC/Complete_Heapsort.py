n = int(input())
arr = list(map(int,input().split()))
l = []
def shiftdown(arr,n,i):
	lc = 2*i+1
	rc = 2*i+2
	if rc < n and lc < n and arr[i] < arr[rc] and arr[i]< arr[lc]:
		return
	elif rc < n:
		if arr[rc] < arr[lc]:
			if arr[i] > arr[rc]:
				arr[i],arr[rc] = arr[rc],arr[i]
				shiftdown(arr,n,rc)
			return
		else:
			if arr[i] > arr[lc]:
				arr[i],arr[lc] = arr[lc],arr[i]
				shiftdown(arr,n,lc)
			return
	elif lc < n:
		if arr[i] > arr[lc]:
			arr[i], arr[lc] = arr[lc],arr[i]
			return
	else:
		return


def makeheap(arr,n,i):
	lc = 2*i+1
	rc = 2*i+2
	if rc < n:
		makeheap(arr,n,lc)
		makeheap(arr,n,rc)
		shiftdown(arr,n,i)
	elif lc < n:
		makeheap(arr,n,lc)
		shiftdown(arr,n,i)
	return


def heapsort(arr,n,l):
	if n == 1:
		l.append(arr[0])
		return
	l.append(arr.pop(0))
	arr.insert(0,arr.pop())
	shiftdown(arr,n-1,0)
	heapsort(arr,n-1,l)
	return

makeheap(arr,n,0)
print(arr)
heapsort(arr,n,l)
print(l)

	
	
	
				