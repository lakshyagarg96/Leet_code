class Solution(object):
    def smallestEqual(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        o_l = []
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                o_l.append(i)
        print (o_l)
        if len(o_l) != 0:
            return min(o_l)
        else:
            return (-1)
        