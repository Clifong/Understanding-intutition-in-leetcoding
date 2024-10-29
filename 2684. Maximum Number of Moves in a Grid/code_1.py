"""
Intuition:

For questions like this involving traversal and optimal quantity,
which in this case involves maximising moves, you would want to try to
check if overlapping subproblems can exist.

Using
[ 2,  4,   3,     5]
[ 5,  4,   9,     3]
[ 3,  4,   2,    11]
[10,  11,  13,    15]

We start at (0, 0). 1st index = row and 2nd index = column

(0, 0) -> *(0, 1) -> (1, 2)*
(1, 0) -> (1, 1) -> (1, 2)

(2, 0) -> *(0, 1) -> (1, 2)*
(2, 0) -> (2, 1) -> *(3, 2) -> (3, 3)*

(3, 0) -> (3, 1) -> *(3, 2) -> (3, 3)*

Notice that there are indeed repeated subproblems because of
overlapping paths. Thus 100% a DP question.Therefore, memoize
the row and column.                   
"""

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        
        #A wrapper that is the equivalent of the standard memoization
        #technique
        @lru_cache(None)
        def dp(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return 0
            else:
                best = 0
                if r - 1 >= 0 and c + 1 < len(grid[0]) and grid[r - 1][c + 1] > grid[r][c]:
                    best = max(best, 1 + dp(r - 1, c + 1))
                if c + 1 < len(grid[0]) and grid[r][c + 1] > grid[r][c]:
                    best = max(best, 1 + dp(r, c + 1))
                if r + 1 < len(grid) and c + 1 < len(grid[0]) and grid[r + 1][c + 1] > grid[r][c]:
                    best = max(best, 1 + dp(r + 1, c + 1))
                return best

        ideal = 0
        for i in range(len(grid)):
            ideal = max(ideal, dp(i, 0))
        return ideal