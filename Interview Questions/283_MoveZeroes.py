class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = [ i for i in range(len(nums)) if nums[i] == 0 ]
        for i in range(len(l)):
            nums.pop(l[i] - i)
            nums.append(0)
        
            
