class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # corner cases: empty s or t
        if not s: return True
        if not t: return False
        
        # create a grid for dynamic programing: s rows x t cols
        grid = [[0 for cols in range(0, len(t))] for rows in range(0, len(s))]
        
        # itterate throught the grid (dynamic programing)
        for row in range(0, len(s)):
            for col in range(0, len(t)):
                if s[row] != t[col]:
                    grid[row][col] = max(grid[row][col], grid[row][col-1], grid[row-1][col])
                else:
                    grid[row][col] = max(grid[row][col] + 1, grid[row-1][col-1] + 1)
        
        # print the grid
        for i in range(0, len(grid)):
            print(grid[i])
        
        # calculate the max element for the grid and compare it with the s subsequence length
        max_subsequence = max(map(max, grid))
        return True if len(s) == max_subsequence else False