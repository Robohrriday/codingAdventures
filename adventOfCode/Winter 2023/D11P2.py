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

numreg = (len(rows)+1)*(len(cols)+1) # (8+1)*(11+1) = 108
matching = dict()

for i in range(0,140):
    for j in range(0,140):
        if uni[i][j] == '#':
            if i > rows[-1]:
                a = len(rows)
            else:
                for k in range(0,len(rows)):
                    if i < rows[k]:
                        a = k
                        break
            if j > cols[-1]:
                b = len(cols)
            else:
                for k in range(0,len(cols)):
                    if j < cols[k]:
                        b = k
                        break
            matching[(i,j)] = (a,b)

p = 0
locs = list(matching.keys())
for i in range(0,len(matching)-1):
    for j in range(i+1, len(matching)):
        p += abs(locs[i][0]-locs[j][0]) + abs(locs[i][1]-locs[j][1]) + 999999*(abs(matching[locs[i]][0]-matching[locs[j]][0]) + abs(matching[locs[i]][1]-matching[locs[j]][1]))
print(p)