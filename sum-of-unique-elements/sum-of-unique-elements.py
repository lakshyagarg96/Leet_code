class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        e_d = {}
        sum_num = 0
        for i in nums:
            e_d[i] = e_d.get(i, 0) + 1
        for j in e_d:
            if e_d[j] == 1:
                sum_num += j
        return sum_num
        
        