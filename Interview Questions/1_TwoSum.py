class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            for j in range (i+1,len(nums)):
                if(target == nums[i]+nums[j]):
                    res.append(i)
                    res.append(j)
                    return res
                    
        