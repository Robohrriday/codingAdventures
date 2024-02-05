n = int(input())
arr = list(map(int,input().split()))
v = int(input())

def s(arr,n,i,v):
	if arr[i] == v:
		print(i)
		return True
	lc = 2*i+1
	rc = 2*i+2
	r1 = True
	r2 = True
	if rc < n:
		r1 = s(arr,n,rc,v)
		r2 = s(arr,n,lc,v)
		return r1 or r2
	elif lc < n:
		r1 = s(arr,n,lc,v)
		return r1
	else:
		return False

r = s(arr,n,0,v)
if not r:
	print(-1)
	
	