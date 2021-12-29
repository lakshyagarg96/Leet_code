class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        expected = sorted(heights, reverse=False)
        counter = 0
        print (expected)
        for i,j in zip (heights,expected):
            if i != j:
                counter += 1
        return counter
        
        