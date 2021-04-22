class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n<=0):
            return False
        maxpower = 3 ** 100
        if(maxpower % n == 0):
            return True
        else:
            return False
