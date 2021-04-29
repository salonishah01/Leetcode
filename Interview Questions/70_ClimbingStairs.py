class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n==1):
            return 1
        f=[1,2]
        for i in range(2,n):
            f.append(f[i-1]+f[i-2])
            
        return f[-1]
        
