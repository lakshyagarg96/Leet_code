class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        e_d = {}
        o_l = []
        for i in nums:
            if i in e_d:
                e_d[i] = e_d[i] + 1
            else:
                e_d[i] = 1
        print (e_d)
        for k in e_d:
            if e_d[k] > len(nums)/2:
                o_l.append(k)
        return o_l[0]
                