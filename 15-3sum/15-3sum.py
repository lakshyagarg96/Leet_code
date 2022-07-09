class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        triplets = []
        
        #https://leetcode.com/problems/3sum/discuss/2234102/Python-Two-Pointers-Time-O(N2)-or-Space-O(1)-Explained
        for i in range(len(nums)):
            
            if i> 0 and nums[i-1] == nums[i]:
                continue
            
            left = i+1
            right = len(nums)-1
            
            while right > left:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    triplets.append([nums[i],nums[left],nums[right]])
                    left = left +1
                    right = right -1
                    
                    while right> left and nums[left-1] == nums[left]:
                        left = left + 1
                    
                    while right > left and nums[right+1] == nums[right]:
                        right = right - 1
                    
                
                elif current_sum > 0:
                    right = right -1
                
                else:
                    left = left + 1
        
        return triplets
                
            
            