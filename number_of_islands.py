# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
# An island is surrounded by water and is formed by connecting adjacent lands 
# horizontally or vertically. You may assume all four edges of the grid are all 
# surrounded by water.

# Solution:
# Treat matrix as a graph, with all 1s as vertices
# do DFS

# https://www.geeksforgeeks.org/find-number-of-islands/

class Islands():
    def number_of_islands(self, grid):
        """ """

        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])

        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):

        if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] != '1':
            return
        # mark cell as visited to avoid repeating it
        grid[i][j] = '#'
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)

    