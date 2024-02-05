'''
Time:        62     64     91     90
Distance:   553   1010   1473   1074
'''
times = [62,64,91,90]
dists = [553,1010,1473,1074]
prod = 1
for i in range(0,4):
    ways = 0
    for time in range(1, times[i]):
        dist = (times[i]-time)*time
        if dist > dists[i]:
            ways += 1
    prod *= ways
print(prod)