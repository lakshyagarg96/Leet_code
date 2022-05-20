class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        b = set(range(len(nums)+1))
        nums = set(nums)
        
        if len(b) > len(nums):
            return list(b.difference(nums))[0] 
        else:
            return list(nums.difference(b))[0] 