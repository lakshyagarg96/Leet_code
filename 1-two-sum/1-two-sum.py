class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # First method time complexity O(n2)
        # counter = 0
        # for a, i in enumerate(nums):
        #     for b, j in enumerate(nums):
        #         if (a!=b) & (i + j == target):
        #             return a,b
        
        # second method
    
        
        hashmap = dict()
        for i in range(len(nums)):
            hashmap[i] = nums[i]
        print(hashmap)
    
        for j in hashmap:
            target_new = target - hashmap[j]
            if (target_new in hashmap.values()) & (j != hashmap.keys()[hashmap.values().index(target_new) if target_new in hashmap.values() else -1] ):
                return (j, hashmap.keys()[hashmap.values().index(target_new)])