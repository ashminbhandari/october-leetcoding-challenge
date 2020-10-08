# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        if not root: return None

        if (root.val == key):
            #3cases
            #case 1
            if (not root.right and not root.left): return None

            #cse 2
            elif (not root.right): return root.left
            elif(not root.left): return root.right

            #cse3
            #find leftest in the right sub tree
            parent = root
            leftest = root.right
            while(leftest.left):
                parent = leftest
                leftest = leftest.left
            root.val = leftest.val
            if(parent == root):
                root.right = leftest.right
            else:
                parent.left = leftest.right
            return root

        #go ahead and modify and return me the correct nodes
        elif (key > root.val): root.right = self.deleteNode(root.right, key)
        else: root.left = self.deleteNode(root.left, key)

        return root


