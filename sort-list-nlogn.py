class Solution(object):
    def sortList(self, head):

        def splitList(head):
            tmp = head
            slow = head
            fast = head
            while (fast and fast.next):
                tmp = slow
                slow = slow.next
                fast = fast.next.next
            tmp.next = None
            return slow

        def merge(h1, h2):
            if not h1 or not h2:
                return h1 or h2
            if h1.val > h2.val:
                h1, h2 = h2, h1
            head = pre = h1
            h1 = h1.next
            while h1 and h2:
                if h1.val < h2.val:
                    pre.next = h1
                    h1 = h1.next
                else:
                    pre.next = h2
                    h2 = h2.next
                pre = pre.next
            pre.next = h1 or h2
            return head

        def sortList(head):
            if not head or not head.next:
                return head

            s1 = splitList(head)

            sortedA = sortList(head)
            sortedB = sortList(s1)

            return merge(sortedA, sortedB)

        return sortList(head)







