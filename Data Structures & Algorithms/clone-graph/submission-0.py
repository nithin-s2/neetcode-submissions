from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def duplicate(self, node):
        q = deque()
        new = {}
        
        if not node:
            return None

        q.append(node)
        new[node] = Node(node.val)

        while q:
            nod = q.pop()

            # print(new)
            for nei in nod.neighbors:
                if nei not in new:
                    new[nei] = Node(nei.val)
                    q.append(nei)
                new[nod].neighbors.append(new[nei])

        return new

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node:
            new = self.duplicate(node)
            return new[node]
        else:
            return node
        