"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node: return node

        stack = [node]

        visited = set()

        cpy = {}

        while stack:

            n = stack.pop(0)

            if n.val not in cpy:

                cpy[n.val] = Node(n.val, [])

            if n.val not in visited:

                visited.add(n.val)

                for ns in n.neighbors:

                    if ns.val not in cpy:

                        cpy[ns.val] = Node(ns.val, [])

                    cpy[n.val].neighbors.append(cpy[ns.val])

                    stack.append(ns)

        return cpy[node.val]
