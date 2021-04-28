# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        first = ListNode()
        first = head
        cnt = 0
        while(first):
            cnt += 1
            first = first.next
        index = cnt//2
        first = head
        for i in range(index):
            first = first.next
        return first
            
            
