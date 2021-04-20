class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = int("".join(map(str, digits)))
        res = res + 1
        res = list(map(int, str(res)))
        return res
