class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        stack = [root]
        depth = 1
        while len(stack) != 0:
            tmp = []
            for i in range (len(stack)):
                if not stack[i].left and not stack[i].right:
                    return depth
                if stack[i].left:
                    tmp.append(stack[i].left)
                if stack[i].right:
                    tmp.append(stack[i].right)
            depth += 1
            stack = tmp
        return depth
