# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
import copy

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carryover = 0
        rt = None
        tailnode = None
        while(l1 and l2):
            print("step 0")
            sum_ = l1.val + l2.val + carryover
            if(sum_>= 10):
                sum_ %= 10
                carryover = 1
            else:
                carryover = 0
            if(rt is None):
                rt = ListNode(sum_)
                #tailnode = copy.copy(rt)
                tailnode = rt
            else:
                tailnode.next = ListNode(sum_)
                tailnode = tailnode.next
            l1 = l1.next
            l2 = l2.next
        while(l1):
            print("step 1")
            sum_ = l1.val + carryover
            if(sum_>= 10):
                sum_ %= 10
                carryover = 1
            else:
                carryover = 0
            tailnode.next = ListNode(sum_)
            tailnode = tailnode.next
            l1 = l1.next
        while(l2):
            print("step 2")
            sum_ = l2.val + carryover
            if(sum_>= 10):
                sum_ %= 10
                carryover = 1
            else:
                carryover = 0
            tailnode.next = ListNode(sum_)
            tailnode = tailnode.next
            l2 = l2.next
            
        if(carryover == 1):
            tailnode.next = ListNode(1)
        return rt
        

    
# l1_node1 = ListNode(2)
# l1_node2 = ListNode(4)
# l1_node3 = ListNode(3)
# l1_node1.next = l1_node2
# l1_node2.next = l1_node3
# l1_node3.next = None
# l2_node1 = ListNode(5)
# l2_node2 = ListNode(6)
# l2_node3 = ListNode(4)
# l2_node1.next = l2_node2
# l2_node2.next = l2_node3
# l2_node3.next = None

l1_node1 = ListNode(4)
l1_node2 = ListNode(3)
l1_node1.next = l1_node2
l1_node2.next = None
l2_node1 = ListNode(5)
l2_node1.next = None


print("start")
test = Solution()
result = test.addTwoNumbers(l1_node1,l2_node1)
print(result.val)
print(result.next.val)
