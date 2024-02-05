n = int(input())
arr = list(map(int,input().split()))

def merge(l1,l2,n1,n2):
	i = 0
	j = 0
	l3 = []
	while i < n1 and j < n2:
		if l1[i] <= l2[j]:
			l3.append(l1[i])
			i += 1
		elif l1[i] > l2[j]:
			l3.append(l2[j])
			j += 1
	while i < n1:
		l3.append(l1[i])
		i += 1
	while j < n2:
		l3.append(l2[j])
		j += 1
	return l3

def mergesort(arr,low,high):
	if low == high:	
		return [arr[low]]
	mid = (low+high)//2
	l1 = mergesort(arr,low,mid)
	l2 = mergesort(arr,mid+1,high)
	l3 = merge(l1,l2,mid-low+1,high-mid)
	return l3

print(mergesort(arr,0,n-1))

		