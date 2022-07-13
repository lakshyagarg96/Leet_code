# Brute force technique

# def min_value(nums):
#     min_value = 1000000
#     for i in range(len(nums)):
#         if nums[i] < min_value:
#             min_value = nums[i]
#     nums.remove(min_value)
#     return min_value, nums

# class Solution(object):
#     def sortArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         e_l = []
#         for j in range(len(nums)):
#             a,nums = min_value(nums)
#             e_l.append(a)
#         return (e_l)

# merge sort
class Solution(object):

    def merge(self, nums, l, r):
    # this function checks the values in right and left list subpart and creates a new list by taking the minimum values in the left and right sublist
        i = 0
        j = 0
        k = 0
        while i < len(l) and j < len(r):
            
            if l[i] < r[j]:
                nums[k] = l[i]
                i += 1
                k += 1
            else:
                nums[k] = r[j]
                j += 1
                k += 1

        while i < len(l):
            nums[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            nums[k] = r[j]
            j += 1
            k += 1

        return nums

    def mergeSort(self, nums):

        if len(nums) > 1:
            mid = len(nums)//2
            l = nums[:mid]
            r = nums[mid:]
            self.mergeSort(l)
            self.mergeSort(r)
            return self.merge(nums, l, r)

    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 1:
            return nums

        return self.mergeSort(nums)
        