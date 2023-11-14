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
x = 1
c = 0
s = 0
for e in l:
    if e[0] == 'n':
        if c in [20,60,100,140,180,220]:
            s = s + c*x
        c += 1
    elif e[0] == 'a':
        if c in [20,60,100,140,180,220]:
            s = s + c*x
        c += 1
        if c in [20,60,100,140,180,220]:
            s = s + c*x
        x = x + int(e[e.index(" ")+1:])
        c += 1
print(s)

# 15260