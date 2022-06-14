class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        e_l = []
        for i in range(1,n+1):
            # print (i)
            if i % 15 == 0:
                e_l.append('FizzBuzz')
            elif i % 3 == 0:
                e_l.append('Fizz')
            elif i%5 == 0:
                e_l.append('Buzz')
            else:
                e_l.append(str(i))
        return e_l
                
                    
                