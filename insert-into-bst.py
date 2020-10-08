class Solution(object):
    def insertIntoBST(self, root, val):
        if (root == None):
            return TreeNode(val)

        def helper(root, val):
            if (root.val > val):
                if (root.left): helper(root.left, val)
                else:
                    root.left = TreeNode(val)
                    return
            else:
                if(root.right): helper(root.right, val)
                else:
                    root.right = TreeNode(val)
                    return

        helper(root, val)

        return root
