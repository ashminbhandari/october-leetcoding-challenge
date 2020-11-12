class Solution(object):
    def constructFromPrePost(self, pre, post):
        if not pre: return None
        root = TreeNode(pre[0])
        if len(pre) == 1: return root
        idx = post.index(pre[1]) + 1 #idx of second element in pre in post
        root.left = self.constructFromPrePost(pre[1 : idx + 1], post[ : idx])
        root.right = self.constructFromPrePost(pre[idx + 1 : ], post[idx : -1])
        return root