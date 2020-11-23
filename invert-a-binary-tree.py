class Solution(object):
    def invertTree(self, root):
        def help(root):
            if not root:
                return
            help(root.left)
            help(root.right)
            tmp = root.left
            root.left = root.right
            root.right = tmp
        help(root)
        return root