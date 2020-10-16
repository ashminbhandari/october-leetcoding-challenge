# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        #at each point in the tree, i have to decide whether or not i want to rob this node or not
        #if i do rob this node, then i cannot rob the node below it
        #if i do not rob this rode, then i can rob the node below it
        #we calculate this bottom up, basically dissecting into subprobleming this and targeting it at that level
        def dfsRob(root):
            if not root:
                return [0,0] #rob and not rob are both 0 at this point

            #rob left, this is to get the max possible rob value to the left
            maxRobLeft = dfsRob(root.left)

            #rob right, this is to get the max possible rob value to the right
            maxRobRight = dfsRob(root.right)

            #if I do decide to rob then, I would have to take the sum of two not robs below + the current node value because we decided to rob this one
            ifRob = root.val + maxRobLeft[1] + maxRobRight[1]

            #if i do not rob this then there a myriad of choices that i can do, get the max of these choices
            robLeft = maxRobLeft[0]
            robRight = maxRobRight[0]
            notRobLeft = maxRobLeft[1]
            notRobRight = maxRobRight[1]

            ifNotRob = max(robLeft + robRight, robLeft + notRobRight, notRobLeft + robRight, notRobLeft + notRobRight)

            return (ifRob, ifNotRob)

        return max(dfsRob(root))








