class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        return 1.0*(sum(salary)-min(salary)-max(salary))/(len(salary)-2)
        
