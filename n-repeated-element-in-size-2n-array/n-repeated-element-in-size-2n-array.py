class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print (nums)
        n = len(nums)/2
        e_d = {}
        for i in nums:
            e_d[i] = e_d.get(i, 0) + 1
        for j in e_d:
            if e_d[j] == n:
                return j
            
        