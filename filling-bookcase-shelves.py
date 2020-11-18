class Solution(object):
    def minHeightShelves(self, books, shelf_width):
        self.m = {}
        def helpRecur(books, i):
            if i in self.m: return self.m[i]
            if i >= len(books): return 0
            w, cmh, minh, j = 0, 0, sys.maxint, i
            while (j < len(books) and w + books[j][0] <= shelf_width):
                w += books[j][0]
                cmh = max(books[j][1], cmh)
                minh = min(cmh + helpRecur(books, j + 1), minh)
                j += 1
            self.m[i] = minh
            return self.m[i]
        return helpRecur(books, 0)