from random import randrange
from tkinter import *

DELTA = 20
DIST = 10
moving = 0

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
