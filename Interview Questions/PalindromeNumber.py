class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x < 0):
            return bool(0)
        ori = x
        rev = 0
        while (x):
            dig = x % 10
            rev = rev * 10 + dig
            x = x//10
        if(rev == ori):
            return bool(1)
        else:
            return bool(0)
        
