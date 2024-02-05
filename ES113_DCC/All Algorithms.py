# All Algorithms

n = int(input())
arr = list(map(int,input().split()))

# Search Algorithms

# Binary Search 
# Time Complexity: O(log(n))
# Space Complexity: O(1)



def bianry_search(arr,low,high,k):
	if low == high:
		if arr[low] == k:
			return low
		else:
			return -1
	mid = (low+high)//2
	if arr[mid] == k:
		return mid
	elif arr[mid] < k:
		return binary_search(arr,mid+1,high,k)
	else:
		return binary_search(arr,low,mid,k)

# Sorting Algorithms

# Bubble Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)


def bubble_sort(arr,n):
	j = 0
	while j < n-1:
		i = 0
		while i < n-1-j:
			if arr[i] > arr[i+1]:
				arr[i],arr[i+1] = arr[i+1],arr[i]
			i += 1
		j += 1
	return


# Insertion Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)


def insertion_sort(arr,n):
	i = 0
	while i < n-1:
		if arr[i] > arr[i+1]:
			arr[i],arr[i+1] = arr[i+1],arr[i]
			j = i
			while j > 0:
				if arr[j] < arr[j-1]:
					arr[j],arr[j-1] = arr[j-1],arr[j]
					j -= 1
				else:
					break
		i += 1
	return

# Merge Sort
# Time Complexity: O(nlog(n))
# Space Complexity: O(n)

# Merge
# Time Complexity: O(n1+n2)
# Space Complexity: O(1)

def merge(l1,l2,n1,n2):
	i = 0
	j = 0
	l3 = []
	while i < n1 and j < n2:
		if l1[i] < l2[j]:
			l3.append(l1[i])
			i += 1
		elif l1[i] > l2[j]:
			l3.append(l2[j])
			j += 1
		else:
			l3.append(l1[i])
			i += 1
			j += 1
	while i < n1:
		l3.append(l1[i])
		i += 1
	while j < n2:
		l3.append(l2[j])
		j += 1
	return l3

def merge_sort(arr,low,high):
	if low == high:
		return [arr[low]]
	mid  = (low+high)//2
	l1 = merge_sort(arr,low,mid)
	l2 = merge_sort(arr,mid+1,high)
	l3 = merge(l1,l2,mid-low+1,high-mid)
	return l3


# Heap Sort
# Time Complexity: O(nlog(n))
# Space Complexity: O(1)

# Shiftdown
# Time Complexity: O(log(n))
# Space Complexity: O(1)

def shiftdown(arr,n,i):
	lc = 2*i+1
	rc = 2*i+2
	if rc < n and lc < n and arr[i] < arr[lc] and arr[i] < arr[rc]:
		return
	elif rc < n:
		if arr[rc] > arr[lc]:
			if arr[i] > arr[lc]:
				arr[i],arr[lc] = arr[lc],arr[i]
				shiftdown(arr,n,lc)
			return
		else:
			if arr[i] > arr[rc]:
				arr[i],arr[rc] = arr[rc],arr[i]
				shiftdown(arr,n,rc)
			return
	elif lc < n:
		if arr[i] > arr[lc]:
			arr[i],arr[lc] = arr[lc],arr[i]
		return
	else:
		return

def heap_sort(arr,n,i):
	lc = 2*i+1
	rc = 2*i+2
	if rc < n:
		heap_sort(arr,n,lc)
		heap_sort(arr,n,rc)
		shiftdown(arr,n,i)
		return
	elif lc < n:
		heap_sort(arr,n,lc)
		shiftdown(arr,n,i)
		return
	else:
		return


# Quick Sort
# Time Complexity: O(n^2)
# Time COmplexity (Avg case): O(nlog(n))
# Space Complexity: O(1)

# Partition
# Time Complexity: O(n)
# Space Complexity: (1)

def partition(arr,low,high):
	p = arr[low]
	i = low+1
	j = high
	while i < j:
		while i < j and arr[i] < p:
			i += 1
		while i < j and arr[j] > p:
			j -= 1
		if i == j:
			break
		else:
			arr[i],arr[j] = arr[j],arr[i]
			i += 1
			j -= 1
	if i == low+1:
		if arr[i] < p:
			arr[i],arr[low] = arr[low],arr[i]
			return i
		else:
			return low
	elif i == high:
		if arr[i] < p:
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

def quick_sort(arr,low,high):
	if low == high:
		return
	pi = partition(arr,low,high)
	if pi == low:
		quick_sort(arr,pi+1,high)
		return
	elif pi == high:
		quick_sort(arr,low,pi-1)
		return
	else:
		quick_sort(arr,pi+1,high)
		quick_sort(arr,low,pi-1)
		return






				