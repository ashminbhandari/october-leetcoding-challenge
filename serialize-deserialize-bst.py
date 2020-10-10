class Codec:
    idx = 0

    def serialize(self, root):
        if root == None: return "_"
        return str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)

    def deserialize(self, data):
        data = data.split(',')
        def dfs(data):
            if (data[self.idx] == "_" or self.idx >= len(data)): return None
            root = TreeNode(data[self.idx])
            self.idx += 1
            root.left = dfs(data)
            self.idx += 1
            root.right = dfs(data)
            return root
        return dfs(data)