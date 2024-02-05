s = '''noop
noop
noop
noop
addx 5
addx 5
noop
addx 3
noop
addx 2
addx 1
noop
noop
noop
addx 4
addx -4
addx 7
addx 7
noop
addx -2
addx 5
addx -23
addx 26
addx -38
noop
noop
noop
addx 3
addx 2
addx 5
addx 2
addx 9
addx -8
addx 2
addx 16
addx -9
addx 3
addx -2
addx 2
noop
addx 7
addx -2
addx 5
addx 2
addx 3
noop
addx -40
addx 5
noop
addx 2
addx -6
addx 11
addx -1
addx 3
addx 3
noop
noop
noop
addx 5
addx -2
noop
addx 7
addx 8
addx -2
addx -3
addx 5
addx 2
addx -10
addx -26
addx 1
noop
addx 8
addx -5
addx 4
addx 3
addx -3
addx 4
addx 2
addx -9
addx 16
addx 2
noop
addx 3
addx 3
addx 2
addx -2
addx 5
addx 2
addx 2
noop
addx -38
addx 34
addx -28
addx -2
addx 5
addx 2
addx 3
addx -2
addx 2
addx 7
noop
noop
addx -4
addx 5
addx 2
addx 15
addx -8
addx 3
noop
addx 2
addx -8
addx 9
addx -38
addx 26
noop
addx -18
noop
noop
addx 4
addx 4
addx -3
addx 2
addx 20
addx -12
noop
noop
noop
addx 4
addx 1
noop
addx 5
noop
noop
addx 5
noop
noop
noop
noop
noop
noop
noop'''

l = s.split('\n')
x_l = []
x = 1
crt_l = []
crt = ''
for e in l:
    if e[0] == 'n':
        x_l.append(x)
    elif e[0] == 'a':
        x_l.append(x)
        x_l.append(x)
        x = x + int(e[e.index(" ")+1:])

sprite_pos = [[p-1,p,p+1] for p in x_l]

for i in range(240):
    if i % 40 == 0 and i != 0:
        crt_l.append(crt)
        crt = ''
    if i % 40 in sprite_pos[i]:
        crt = crt + '#'
    else:
        crt = crt + '.'
crt_l.append(crt)
print('\n'.join(crt_l))

# PGHFGLUG