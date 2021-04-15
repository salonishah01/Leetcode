import math
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 0
        if(x < 0):
            x = 0 - x
            flag = 1
        rev = 0
        while(x):
            dig = x % 10;
            rev = rev* 10 + dig
            x = x//10
        if(flag):
            rev = 0 - rev
        if(rev >= pow(-2,31) and rev <= pow(2,31)-1):
            return rev
        else:
            return 0
    
        
