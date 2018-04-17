# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        output = []
        if hasattr(l1,"next"):
            while l1.next!=None:
                output.append(l1.val)
                l1 = l1.next
            output.append(l1.val)
        if hasattr(l2,"next"):
            while l2.next!=None:
                output.append(l2.val)
                l2 = l2.next
            output.append(l2.val)
        token = 0
        while token==0:
            token =1
            for i in range(len(output)-1):
                if output[i]>output[i+1]:
                    temp = output[i]
                    output[i] = output[i+1]
                    output[i+1] = temp
                    token*=0
                else:
                    token*=1
        return output