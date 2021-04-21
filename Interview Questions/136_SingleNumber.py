class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            k = nums.count(nums[i])
            if(k == 1):
                return nums[i]
            
        
