import numpy as np
import random as rand
import matplotlib.pyplot as plt

def update_cells(list_coord, l):
    i = 0
    while i < len(list_coord):
        c = list_coord[i]
        direction = rand.randint(0, 1)
        zin = rand.randint(0, 1)
        if direction: 
            if zin:
                c[0] += 1
            else:
                c[0] -= 1
        else:
            if zin:
                c[1] += 1
            else:
                c[1] -= 1
        if c[0] < 0 or c[0] >= l or c[1] < 0 or c[1] >= l:
            del list_coord[i]
        else:
            i += 1
         
    return list_coord

def stationary_cells(list_coord, list_stat):
    k = 0
    while k < len(list_coord):
        x = list_coord[k][0]
        y = list_coord[k][1]
        stat = False
        for i in [x-1, x+1]:
            if 0 <= i < len(list_stat): 
                if list_stat[i][y]:
                    stat = True
        for j in [y-1, y+1]:
            if 0 <= j < len(list_stat): 
                if list_stat[x][j]:
                    stat = True
        if stat:
            list_stat[x][y] = 1
            del list_coord[k]
        else:    
            k += 1  
    return list_coord, list_stat

def aanvulling(list_coord, L, l):
    while len(list_coord) < L:
        direction = rand.randint(0, 1)
        zin = rand.randint(0, 1)
        positie = rand.randint(0, l-1)
        if direction: 
            if zin:
                list_coord.append([l-1, positie])
            else:
                list_coord.append([0, positie])
        else:
            if zin:
                list_coord.append([positie, l-1])
            else:
                list_coord.append([positie, 0])
    return list_coord

L = 100
l = 200
steps = 1000000
grid = [[0 for _ in range(l)] for _ in range(l)]
grid[l//2][l//2] = 1

cells = aanvulling([], L, l)

for _ in range(steps):
    update_cells(cells, l)
    stationary_cells(cells, grid)
    aanvulling(cells, L, l)

plt.imshow(grid, cmap="gray")
plt.show()

