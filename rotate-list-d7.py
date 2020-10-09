class Solution(object):
    def rotateRight(self, head, k):
        if (not head):
            return head

        #create stack of llist values
        h = head
        stack = []
        while (head):
            stack.append(head.val)
            head = head.next

        #if the displacement circulates
        if (k > len(stack)):
            k = k % len(stack)

        #set vals according to displaced indices
        head = h
        idx = 0
        while(head):
            dis = len(stack) - k + idx
            if(dis >= len(stack)):
                dis = idx - k
            head.val = stack[dis]
            head = head.next
            idx += 1

        #reset back
        head = h
        return head
