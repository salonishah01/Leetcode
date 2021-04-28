# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        k = []
        while(head):
            k.append(head.val)
            head = head.next
        reversed_k = k[::-1]
        if k == reversed_k:
            return True
        else:
            return False
            
        
