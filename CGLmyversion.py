# Version of Conway's Game of life
# Author: Matthew Pfannenstiel matt.c.pfannenstiel@gmail.com, Jan 2016


import golly as g


def neighborcount(x, y):
    c = 0
    if g.getcell(x - 1, y) == 1:
        c += 1
    if g.getcell(x - 1, y - 1) == 1:
        c += 1
    if g.getcell(x, y - 1) == 1:
        c += 1
    if g.getcell(x - 1, y + 1) == 1:
        c += 1
    if g.getcell(x, y + 1) == 1:
        c += 1
    if g.getcell(x + 1, y + 1) == 1:
        c += 1
    if g.getcell(x + 1, y - 1) == 1:
        c += 1
    if g.getcell(x + 1, y) == 1:
        c += 1
    return c


def rules(x, y, u):
    i = neighborcount(x, y)
    if i == 3 and g.getcell(x, y) == 0:
        u[x][y] = 1
    if i > 3 and g.getcell(x, y) == 1:
        u[x][y] = 0
    if i < 2 and g.getcell(x, y) == 1:
        u[x][y] = 0
    if i == (2 | 3) and g.getcell(x, y) == 1:
        u[x][y] = g.getcell(x, y)
    return u


def main(width, height, update):
    w = width
    h = height
    x = 0
    i = 0
    while x < w:
        y = 0
        while y < h:
            update = rules(x, y, update)
            y += 1
        x += 1
    while i < w:
        j = 0
        while j < h:
            g.setcell(i, j, update[i][j])
            j += 1
        i += 1
    g.update()
    return update


try:
    g.new("Conway's Game of life")
    maxsize = 100000
    count = 0
    width = int( g.getstring("Enter a width for the game of life:", "10") )
    height = int( g.getstring("Enter a height for the game of life:", "10") )
    g.select([0, 0, width, height])
    g.randfill(25)
    update = [[0 for x in range(width + 1)] for x in range(height + 1)]
    while count < maxsize:
        g.show("In main " + str(count))
        update = main(width, height, update)
        count += 1


finally:
    g.note("Goodbye")
