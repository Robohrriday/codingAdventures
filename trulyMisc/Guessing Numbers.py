import random

'''
# ********************* Random Guess, Random Choice ********************* 
lg = []
for i in range(10000):
    l = [i for i in range(1,11)]
    c = random.choice(l)
    g = random.choice(l)
    cnt = 1
    while True:
        if g == c:
            break
        elif g>c:
            for e in l[l.index(g):]:
                l.remove(e)
        elif g<c:
            for e in l[:l.index(g)+1]:
                l.remove(e)
        g = random.choice(l)
        cnt += 1
    lg.append(cnt)
print((sum(lg))/len(lg))

# Avg = 3.44 guesses


# ********************* Random Choice, Binary Search Guess *********************
lg = []
for i in range(10000):
    l = [i for i in range(1,9)]
    c = random.choice(l)
    cnt = 1
    g = (l[0]+l[-1])//2

    while True:
        if g == c:
            break
        elif g>c:
            for e in l[l.index(g):]:
                l.remove(e)
        elif g<c:
            for e in l[:l.index(g)+1]:
                l.remove(e)
        g = (l[0]+l[-1])//2
        cnt += 1
    lg.append(cnt)
print(sum(lg)/len(lg))

# Avg = 2.61 guesses
'''