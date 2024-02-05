def bsi(arr,low,high,k):
	if low == high:
		if arr[low] == k:
			return low
		else:
			return -1
	mid = (low+high)//2
	if arr[mid] == k:
		return mid
	elif arr[mid]>k:
		return bsi(arr,low,mid,k)
	else:
		return bsi(arr,mid+1,high,k)

def bsd(arr,low,high,k):
	if low == high:
		if arr[low] == k:
			return low
		else:
			return -1
	mid = (low+high)//2
	if arr[mid] == k:
		return mid
	elif arr[mid] > k:
		return bsd(arr,mid+1,high,k)
	else:
		return bsd(arr,low,mid,k)

def floor_ceil(arr,low,high,k):
	if low == high:
		return (low,'u')
	mid = (low+high)//2
	if arr[mid] == k:
		return (mid,'e')
	elif arr[mid+1] == k:
		return (mid+1,'e')
	elif arr[mid]>k:
		return floor_ceil(arr,low,mid,k)
	elif arr[mid]<k and arr[mid+1]>k:
		return (mid,'f')
	elif arr[mid+1]<k:
		return floor_ceil(arr,mid+1,high,k)
					

n = int(input())
arr = list(map(int,input().split()))
k = int(input())
i,d = floor_ceil(arr,0,n-1,k)

if d == 'e':
	print(arr[i],arr[i])
elif d == 'f':
	print(arr[i],arr[i+1])
else:
	if i == 0:
		print('-infty',arr[i])
	elif i == n-1:
		print(arr[i],'infty')
				
				