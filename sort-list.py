class Solution(object):
    def sortList(self, head):
        if not head: return head
        h = head
        elems = []
        while (head):
            elems.append(head.val)
            head = head.next
        elems.sort()
        head = h
        i = 0
        while (head):
            head.val = elems[i]
            head = head.next
            i += 1
        head = h
        return head