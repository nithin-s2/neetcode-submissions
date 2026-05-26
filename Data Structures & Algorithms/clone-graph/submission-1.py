"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def duplicate(self, node):
        new_node = {}
        q = deque()
        if not node:
            return None
        q.append(node)
        new_node[node] = Node(node.val)
        while q:
            cur = q.pop()
                
            for nei in cur.neighbors:
                if nei not in new_node:
                    new_node[nei] = Node(nei.val)
                    q.append(nei)
                new_node[cur].neighbors.append(new_node[nei])
        return new_node[node]
            

            


    
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node:
            new_node = self.duplicate(node)
            return new_node
        else:
            return node