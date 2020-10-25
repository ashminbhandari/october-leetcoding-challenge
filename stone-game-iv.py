class Solution(object):
    mem = {}
    def winnerSquareGame(self, n):
        self.mem = {}
        if math.sqrt(n) % int(math.sqrt(n)) == 0: return True
        def moveTree(n):
            if n in self.mem:
                return self.mem[n]
            for i in range(1, 316):
                if i * i <= n:
                    if not moveTree(n - i * i):
                        self.mem[n] = True
                        return self.mem[n]
            self.mem[n] = False
            return self.mem[n]
        return moveTree(n)         