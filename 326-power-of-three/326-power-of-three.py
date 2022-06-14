class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        remainder = n
        counter = 0
        if n == 0:
            return False
        while counter < 100:
            number = 3 ** counter
            counter = counter + 1 
            if number == n:
                return True
            