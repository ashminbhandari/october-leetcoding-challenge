class Solution(object):
    def longestDiverseString(self, a, b, c):
        heap = []
        if a != 0: heap.append([a, 'a'])
        if b != 0: heap.append([b, 'b'])
        if c != 0: heap.append([c, 'c'])

        idx, st = 0, ''

        while (True):
            heap.sort(reverse=True)
            idx = 1 if len(st) >= 2 and st[-1] == st[-2] == heap[0][1] else 0
            if heap[idx][0]:
                st += heap[idx][1]
                heap[idx][0] -= 1
            else:
                break
        return st