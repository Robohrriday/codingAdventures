n = int(input())
arr = list(map(int,input().split()))

f = True
i = 0
while i < n:
	lc = 2*i+1
	rc = 2*i+2
	if rc < n and lc < n:
		if arr[i] < arr[lc] and arr[i] < arr[rc]:
			i += 1
			continue
		else:
			f = False
			break
	elif lc < n:
		if arr[i] < arr[lc]:
			i += 1
			continue
		else:
			f = False
			break
	else:
		i += 1
if f:
	print('Heap')
else:
	print('Not Heap')
		
		
	
	
		
		
	


				