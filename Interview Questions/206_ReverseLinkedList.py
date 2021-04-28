# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        list1 = []
        first = head
        while(first):
            list1.append(first.val)
            first = first.next
        i = 0
        list1 = list1[::-1]
        first = head
        while(first):
            first.val=list1[i]
            first = first.next
            i = i +1
        
        return head
