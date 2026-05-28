from collections import deque, defaultdict
class Solution:

    def is_valid(self, curr, limit, seen, heights):
        if 0 <= curr[0] < limit[0] and 0 <= curr[1] < limit[1]:
            if curr not in seen:
                return True
            return False
        return False

    def _append(self, curr, q, seen):
        q.append(curr)
        seen.add(curr)
        return q, seen
    
    def _add_property(self, parent, curr, limit, meta):
        if curr[0] == 0 or curr[1] == 0:
            meta[parent].add("p")
        if curr[0] == limit[0]-1 or curr[1] == limit[1]-1:
            meta[parent].add("a")
        return meta

    def find_flow(self, curr, limit, heights, meta):

        directions = (
            (-1,0),
        (0,-1),     (0,1),
            (1,0)
        )

        seen = set()
        q = deque()
        q, seen = self._append(curr, q, seen)
        z = 0

        while q:
            coord = q.pop()
            meta = self._add_property(curr, coord, limit, meta)
            for idx,_dir in enumerate(directions):
                i = coord[0]+_dir[0]
                j = coord[1]+_dir[1]
                if self.is_valid((i,j), limit, seen, heights):
                    if heights[coord[0]][coord[1]] >= heights[i][j]:
                        # if coord in meta:
                            
                        q, seen = self._append((i,j), q, seen)
                        meta = self._add_property(curr, (i,j), limit, meta)
                        # self.new_meta[curr].append((i,j))
                    else:
                        continue
                if len(meta[curr]) > 1:
                    break 
            # z += 1
            # if z >5:
            #     break
        return meta
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r = len(heights)
        c = len(heights[0])

        meta = defaultdict(set)
        # self.new_meta = defaultdict(list)

        for i in range(r):
            for j in range(c):
                # if (i,j) in seen:
                #     continue
                meta = self.find_flow((i,j), (r,c), heights, meta)
                # break
            # break

        # print(meta)
        # print(self.new_meta)
        output = []
        for coord,prop in meta.items():
            if len(prop) > 1:
                output.append(coord)


        return output
                
        