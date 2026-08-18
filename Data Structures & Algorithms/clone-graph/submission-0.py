"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        start = node
        oTon = {}
        stack = [start]
        visited = set()
        visited.add(start)

        # Creating a copy of the nodes
        while stack:
            node = stack.pop()
            oTon[node] = Node(val=node.val)
            for n_nei in node.neighbors:
                if n_nei not in visited:
                    visited.add(n_nei)
                    stack.append(n_nei)
        
        #Creating edges - copy of neighs
        for oldNode, newNode in oTon.items():
            for nei in oldNode.neighbors:
                new_nei = oTon[nei] # grab copy from hashmap
                newNode.neighbors.append(new_nei)
            
        return oTon[start]


                    

        