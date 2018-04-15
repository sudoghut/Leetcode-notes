# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        count = 0
        output = []
        previous = []
        
        togo_num = 0
        if hasattr(head, "next")==False:
            return head
        if head.next==None:
            return head
        while head.next!=None:
            if count % 2 == 0:
                togo_num = head.next.val
            else:
                togo_num = previous[-1]
            previous.append(head.val)
            output.append(togo_num)
            head = head.next
            count+=1
        if count%2 == 0:
            togo_num = head.val
        else:
            togo_num = previous[-1]
        output.append(togo_num)
        return output