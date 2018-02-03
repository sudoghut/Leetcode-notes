# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        count = 0
        l1_int = 0
        l2_int = 0
        l1_current = l1
        l2_current = l2
        output = []
        while 1:
            if count==0:
                l1_int = l1.val
                l2_int = l2.val
                count+=1    
            print(1)
            print(hasattr(l1_current.next, 'val'))
            print(hasattr(l2_current.next, 'val'))
            if (hasattr(l1_current.next, 'val')==False) and (hasattr(l2_current.next, 'val')==False):
                print(2)
                sum_int = l1_int + l2_int
                for i in str(sum_int):
                    output.insert(0, int(i))
                return output
            if (hasattr(l1_current.next, 'val')==False) or (hasattr(l2_current.next, 'val')==False):
                print(3)
                if (hasattr(l1_current.next, 'val')==False) and (hasattr(l2_current.next, 'val')):
                    l2_current = l2_current.next
                    l2_int = l2_int + l2_current.val*10**count
                    if count==0:
                        l1_int = l1.val
                    count+=1
                    continue
                elif (hasattr(l2_current.next, 'val')==False) and (hasattr(l1_current.next, 'val')):
                    l1_current = l1_current.next
                    l1_int = l1_int + l1_current.val*10**count
                    if count==0:
                        l2_int = l2.val
                    count+=1
                    continue                   


            else:
                l1_current = l1_current.next
                l2_current = l2_current.next
                l1_int = l1_int + l1_current.val*10**count
                l2_int = l2_int + l2_current.val*10**count
                count+=1

    
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
print(test.addTwoNumbers(l1_node1,l2_node1))
