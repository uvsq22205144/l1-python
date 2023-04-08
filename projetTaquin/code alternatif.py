from random import randrange
from tkinter import *

DELTA = 20
DIST = 10
moving_tiles = 0

#Fonction verification des mouvements 
def get_moves(origin, empty):
    i, j = origin
    ii, jj = empty
    delta = (ii - i, jj - j)

    if delta == (0, 0) or delta[0] * delta[1] != 0:
        return None

    norm = max(map(abs, delta))
    dirx, diry = delta[0] // norm, delta[1] // norm

    return [((ii - dirx*k, jj - diry*k), (ii - dirx*(k-1), jj - diry*(k-1)))
            for k in range(norm, 0, -1)]


def animate_tile(item, target_pos, direction):
    global moving_tiles
    start_pos = cnv.coords(item)[:2]  # get the x and y coordinates of the top left corner of the item
    x_diff, y_diff = [t - s for s, t in zip(start_pos, target_pos)]
    u, v = direction
    distance = u * x_diff + v * y_diff
    if distance > DIST:
        cnv.move(item, u * DIST, v * DIST)
        cnv.after(DELTA, animate_tile, item, target_pos, direction)
    else:
        cnv.move(item, x_diff, y_diff)
        moving_tiles -= 1
