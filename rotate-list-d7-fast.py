class Solution(object):
    def rotateRight(self, head, k):
        if not head:
            return head

        h = head

        xlen = 0
        while(head.next):
            head = head.next
            xlen += 1

        if (k > xlen):
            k = k % (xlen + 1)

        #make circular
        head.next = h

        #reset
        head = h

        ylen = 0
        while(head.next):
            if (xlen - k == ylen):
                h = head.next
                head.next = None
                return h
            head = head.next
            ylen += 1



