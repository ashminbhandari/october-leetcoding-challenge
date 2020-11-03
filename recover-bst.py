class Solution(object):
    def recoverTree(self, root):
        self.srted = []
        def helpMe(root):
            if not root: return
            helpMe(root.left)
            self.srted.append(root)
            helpMe(root.right)
        helpMe(root)
        srt = sorted(n.val for n in self.srted)
        for i in range(len(self.srted)):
            self.srted[i].val = srt[i]
        return root







