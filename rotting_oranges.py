
# In a given grid, each cell can have one of three values:

# the value 0 representing an empty cell;
# the value 1 representing a fresh orange;
# the value 2 representing a rotten orange.
# Every minute, any fresh orange that is adjacent 
# (4-directionally) to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a 
# fresh orange.  If this is impossible, return -1 instead.

def orangesRotting(grid):
    """ """

    minutes = 0
    row, col = len(grid), len(grid[0])
    # make a set of the rotting oranges
    # make a set of the fresh oranges
    # while loop
        # cut the while loop if there are fresh and not rotting
        # 
    # make a set of the rotting oranges - this works by looping through

    rotting = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 2}
    fresh = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 1}
    adjacent = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while fresh:
        if not rotting:
            return -1
        # lets explore this - 
        # creating new tuple for rotting by taking the values of rotting and 
        # using the adjacent coordinates to spread out to fresh if the spread out value is fresh
        rotting = {(i + di, j + dj) for i, j in rotting for di, dj in adjacent if (i + di, j + dj) in fresh}
        fresh -= rotting
        minutes += 1
    
    return minutes
        
# grid = [[2,1,1],[1,2,0],[0,1,1]]
# grid = [[2,1,1],[0,1,1],[1,0,1]]
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(orangesRotting(grid))
