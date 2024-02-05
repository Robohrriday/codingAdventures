n = int(input())
arr = list(map(int,input().split()))
v = int(input())
arr.append(v)

def INSERT(arr,i):
	p = (i-1)//2
	if p >= 0:
		if arr[i] < arr[p]:
			arr[i],arr[p] = arr[p],arr[i]
			INSERT(arr,p)
	return

INSERT(arr,n)
print(arr)