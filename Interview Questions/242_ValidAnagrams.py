class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n1 = len(s)
        n2 = len(t)
        
        s = sorted(s)
        t = sorted(t)
        if(n1!=n2):
            return False
        
        for i in range(n1):
            if(s[i]!=t[i]):
                return False
        return True
        
