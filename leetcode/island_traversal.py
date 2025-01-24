"""
Given a 2D array (i.e., a matrix) containing only 1s (land) and 0s (water), 
count the number of islands in it.

An island is a connected set of 1s (land) and is surrounded by either an 
edge or 0s (water). Each cell is considered connected to other cells 
horizontally or vertically (not diagonally).
https://leetcode.com/problems/number-of-islands/
Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
"""
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        count = 0
        visited = set()

        def bfs(r, c):
            queue = deque()
            # initial pair
            visited.add((r, c))
            queue.append((r, c))

            while queue:
                row, col = queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    # cant do this bc r and c might be out of range
                    # island = grid[r][c]
                    # first part needs to be before
                    if (r in range(rows) and c in range(cols) and 
                        grid[r][c] == '1' and (r, c) not in visited):
                        queue.append((r, c))
                        visited.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    count += 1
        return count

# [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
