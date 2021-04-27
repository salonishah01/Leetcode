# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        k = []
        while(head):
            k.append(head.val)
            head = head.next
        res = int("".join(str(x) for x in k), 2)
        return res
            
        
