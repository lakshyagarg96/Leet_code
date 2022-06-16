
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = bin(n)
        counter = 0
        for i in str(n):
            if i == str(1):
                counter = counter + 1
        return counter
        