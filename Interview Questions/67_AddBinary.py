class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = int(a,2)
        b = int(b,2)
        res = a + b
        res = bin(int(res)).replace("0b", "") 
        return res
