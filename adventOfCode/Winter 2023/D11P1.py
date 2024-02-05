s = '''.......#..........................................................................#.........................................................
....................#.........#............#.........................#.......................#..............................................
.#.......................................................#.................#.........................................................#......
..............#.................................#................#....................................................#.....................
..................................#......................................................................#..................................
..................#..................................#.............................#.......#...............................#................
.......#...............................#...................#................................................................................
........................................................................#....................................#........................#.....
..#...........................................................................................................................#.............
............#............#..............................................................................#...................................
...........................................#.....................................................#................#.........................
.....................................................................#...........................................................#..........
...............#....................#.......................................................................................................
#.....................................................#.......................................#............................#..........#.....
.....#................#......#................................................#.............................................................
.......................................#.......................#.......#..............#..................#......#...........................
............................................................................................................................................
...................................................#..............................................#.............................#........#..
..........#........................................................................................................#........................
...............................................#.............................#............#...........#.....................................
....................#..........................................................................................#........#...................
....#.........#............#...............................................................................................................#
....................................#................................#.............#............#...........................................
...............................#..................................................................................#.........................
#...............................................#........#.....................................................................#............
......#........................................................#......................................................#.....................
..........................................#....................................#............................................................
..................#.....................................................................#..................................#.......#........
.............................................................................................#..............................................
.............#........#...........#..........................#............................................#.......#.........................
........#...................#.......................#...................#..................................................................#
.................................................................................#.......................................#..................
................................................................#...........................................................................
...............................................#...........#..........................................#.....#...............................
..........................................#....................................................................................#............
.......#.....#............................................................................#.............................................#...
......................#....................................................#....................................#...........................
.................#...................#................#....................................................................#................
..#...............................................................#...................#.............................#.......................
.............................................................................................#..............................................
.........#..........#.......................................................................................................................
...............................#.........#.......#...............................#.........................................................#
......................................................................................................#...................#.....#...........
........................................................................................#..................#................................
..#.........................................................................................................................................
....................................................................................................................#...................#...
......................#..............................#..........#...........................................................................
......................................................................#..........................................................#..........
#.......................................#......................................................................#............................
.....#..........................#...........................................................................................................
..................#...............................#............................#........................#.................#.................
..........................................................#.................................#...............................................
.......................#..............................................................................................#...........#.....#...
............................................................................................................................................
.......#............................................#.......................................................................................
...............#................#......#......................#......................................#......................................
.....................................................................................#......................................................
............................................................................................................................................
............................................................................................................................................
...#........................................................#...........................#.....#.........................#.........#.........
............................................................................................................................................
...........#..........#......#................................................................................#.............#...............
.......................................#.................................................................................................#..
...............................................#...............#............................................................................
.............................................................................#.....................................#........................
....#..............#..................................................#............#........................................................
..............................#......................#..........................................#.....................................#.....
..............#..........................#...........................................................#......................................
................................................#..............................#..............................#..........#.......#..........
............................................................#...............................................................................
.#........................#.................................................................................................................
...............................#...........................................................#................................................
.............#........................................#........#..................................................#.........................
...........................................#...........................................................#...................#................
.........#.......................................#............................#.......#...................................................#.
.....................................................................#.............................................................#........
...........................................................#................................................................................
.....................................................#......................................#.......#..............#...........#............
............................................................................................................................................
#..........#.....................#..............................................................#........................#..................
...........................#...................#...............................#.....#..................................................#...
................................................................#...........................................................................
.......................................#..................#.......................................................................#.........
...........................................................................................................#................................
......#...............................................#......................#.................#.......................#....................
...............................#..................................#.............................................#....................#......
...........#......................................................................#................#............................#...........
.........................#.........#...............#........................................................................................
.#.........................................#...........................#..................................................................#.
....................#.........................................#.............#...........................................#...................
............................#...................................................................#............................#..............
............................................................................................................................................
.............#..............................................................................#...............#.........................#.....
#......#..........................#...............................................................................#.........................
...............................................#.......................#..................................................................#.
.....................#......................................................................................................................
............................................................#......................#.........................................#......#.......
.........................#............................#................................................................#....................
..#..............................#...............................#..........................................................................
.......................................................................................#.............#..........#...........................
.............#.........................#....................................................................................................
..................................................#...............................#.........................................#...............
...................#..........................................................................#.............................................
.#....................................................#.......#..........................................#......................#.....#.....
...............................#............................................................................................................
..............#....................................................#..........#....................#......................................#.
.........................................................#..............................#..........................#........................
.....#.........................................................................................#.............#..........#...................
..................................#................................................................................................#........
#........................#..................................................................................................................
....................#.......................#................................#..............................................................
...........#.......................................................................#...................#......................#.............
..............................................................#...................................................#.........................
...............................#..................#............................................#............................................
................#.........#.............#............................#....................#................#................................
.#..........................................................................................................................................
........#...................................................................................................................................
..................................#...................................................#.............................................#.......
.................................................................................#..........................................................
.............................#..........................#.....................................#....................#.......................#
........................................#..........................#........................................#...........#.....#.............
......................................................................................................#.....................................
..........#......#.......#....................................................#......................................................#......
.....#...............................................#.................................#........#...........................................
#...........................................#...................................................................................#...........
..............................#..............................#.....................#.......#................................................
......................#.........................#.........................................................................................#.
.......#...........................#.......................................#...............................#............#...................
............#.............................................#........................................#........................................
.....................................................#..............#................#......................................................
............................................................................................................................................
.........................#.................................................................#............#.....................#.............
..................#..........................................................#..................................#......#..................#.
.#.................................................#..........#.........#.........#.........................................................
.......#.........................#.......#..............#..........................................#........................................
.....................#.....#..............................................................................#.................................
...........................................................................#.....................................................#..........
......................................#.........................................................#........................................#..
#...............#...................................#.....................................#............#.................#..................
.............................................#.........................#..........#.............................#...........................'''

uni= s.split('\n')
rows = []
cols = []
for i in range(0,140):
    if uni[i] == 140 * '.':
        rows.append(i)

for i in range(0,140):
    count = 0
    for j in range(0,140):
        if uni[j][i] == '.':
            count += 1
    if count == 140:
        cols.append(i)

expuni = []
for i in range(0,140):
    t = ''
    for j in range(0,140):
        if j in cols:
            t += '..'
        else:
            t += uni[i][j]
    expuni.append(t)

for i in range(140,-1,-1):
    if i in rows:
        expuni.insert(i, 151*'.')

g = 0
locs = []
for i,e in enumerate(expuni):
    for j,f in enumerate(e):
        if f == '#':
            locs.append((i,j))
            g += 1
p = g*(g-1)/2
a = 0
for i in range(0,g-1):
    for j in range(i+1,g):
        a += abs(locs[i][0]-locs[j][0]) +  abs(locs[i][1]-locs[j][1])
print(a)