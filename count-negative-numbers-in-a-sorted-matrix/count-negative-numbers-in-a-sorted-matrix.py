class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        counter = 0
        for j in grid:
            for i in j:
                if i < 0:
                    counter += 1
                    
        return counter
        