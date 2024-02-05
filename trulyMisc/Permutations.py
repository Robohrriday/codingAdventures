a = list(map(int, input('Input Array: ').split(',')))

def permutations(a,n,i):
    
    if i == n-1:
        