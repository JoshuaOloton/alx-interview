#!/usr/bin/python3
""" Island Perimeter """

def amount_of_water(row, col, grid):
    amount = 0
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for i, j in directions:
        try:
            if grid[row + i][col + j] == 0:
               amount += 1
        except IndexError:
           amount += 1

    return amount
        
            
    

def island_perimeter(grid):
    """ Return the perimeter of the island described in grid """
    perimeter = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                perimeter += amount_of_water(row, col, grid)

    return perimeter
                
