class Solution(object):
    def diameterOfBinaryTree(self, tree):
        self.mx = 0
        def findDiameter(tree):
            if not tree: return 0
            left = findDiameter(tree.left) + 1 if tree.left else 0
            right = findDiameter(tree.right) + 1 if tree.right else 0
            if left + right > self.mx:
                self.mx = left + right
            return max(left, right)
        findDiameter(tree)
        return self.mx