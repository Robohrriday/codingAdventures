'''
Time:        62     64     91     90
Distance:   553   1010   1473   1074
'''
ways = 0
for time in range(1, 62649190):
    dist = (62649190-time)*time
    if dist > 553101014731074:
        ways += 1
print(ways)