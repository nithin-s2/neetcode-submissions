from collections import deque
class Solution:


    def is_valid(self, i, j, grid):
        if 0 <= i < self.r and 0 <= j < self.c:
            if grid[i][j] == "1" and ((i,j) not in self.seen):
                return True
            return False
        return False

    def _append(self, i, j):
        self.seen.add((i,j))
        self.q.append((i,j))

    def dfs(self, i, j, grid):

        directions = ((-1,0), (0,1), (1,0), (0,-1))

        self._append(i,j)
        while self.q:
            coord = self.q.pop()
            for _dir in directions:
                ni = coord[0] + _dir[0]
                nj = coord[1] + _dir[1]
                if self.is_valid(ni, nj, grid):
                    self._append(ni, nj)

    def numIslands(self, grid: List[List[str]]) -> int:
        
        self.r = len(grid)
        self.c = len(grid[0])

        self.seen = set()
        self.q = deque()
        
        islands = 0
        for i in range(self.r):
            for j in range(self.c):
                if (i,j) in self.seen:
                    continue
                if grid[i][j] == "1":
                    self.dfs(i,j, grid)
                    islands += 1
        return islands


