import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = re.sub('[\W_]+', '', s)
        reverse_s = s[::-1]
        if(s == reverse_s):
            return True
        return False
        
