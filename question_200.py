class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0

        rows, columns = len(grid), len(grid[0])
        count = 0

        def CountIslands(r, c):
            #boundary check
            if r < 0 or c < 0 or r >= rows or c >= columns or grid[r][c] == "0":
                return  

            #marks as visited
            grid[r][c] = "0"

            #visit 4-direction
            CountIslands(r+1, c)
            CountIslands(r-1, c)
            CountIslands(r, c+1)
            CountIslands(r, c-1)

        #loop for whole grid
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1":
                    count += 1
                    CountIslands(r, c)
        return count 
