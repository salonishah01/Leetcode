class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = [0] * len(nums)
        i = 0 
        j = 1
        for data in nums:
            if(data%2 == 0):
                a[i] = data
                i = i + 2
            else:
                a[j] = data
                j = j + 2
        return a
        
