from collections import deque
class Solution:

    def check(self, coord, bor, heights, prev_height, cells):

        if (coord in cells or coord[0] < 0 or coord[1] < 0 or
         coord[0] >= bor[0] or coord[1] >= bor[1] or 
         heights[coord[0]][coord[1]] < prev_height):
            return True
        return False


    def get_peaks(self, curr, bor, heights, cells):
        directions = ((1,0),(-1,0),(0,1),(0,-1))
        q = deque()

        q.append((curr, heights[curr[0]][curr[1]]))

        while q:
            coord, prev_height = q.popleft()
            if self.check(coord, bor, heights, prev_height, cells):
                continue
            # self.seen.add(coord)
            cells[coord] = heights[coord[0]][coord[1]]
            for _dir in directions:
                ni,nj = coord[0]+_dir[0], coord[1]+_dir[1]
                q.append(((ni,nj), heights[coord[0]][coord[1]]))
            
        # print(self.seen)
        return cells

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r = len(heights)
        c = len(heights[0])

        self.seen = set()
        self.pac = {}
        self.atl = {}

        for i in range(r):
            for j in range(c):
                if i==0 or j==0 :
                    # print(i,j)
                    self.pac = self.get_peaks((i,j), (r,c), heights, self.pac)
                    self.pac[f"{i}{j}"]="-"
                    # print("pac", self.pac)
                if j==c-1 or i==r-1:
                    self.atl = self.get_peaks((i,j), (r,c), heights, self.atl)
                    self.atl[f"{i}{j}"]="-"
                    # print("atl", self.atl)
        output = []
        # print(self.pac)
        # print(self.atl)
        for ele in self.pac:
            if ele in self.atl and isinstance(ele, tuple):
                output.append(ele)
        # print(output)
        return output
