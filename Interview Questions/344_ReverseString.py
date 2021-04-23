class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        k = len(s)
        for i in range(k//2):
            temp = s[i]
            s[i] = s[k-1-i]
            s[k-1-i] = temp
            
