
def square(n):
    """
    :type n: int
    :rtype: bool
    """
    counter = 0
    for i in str(n):
        counter = counter + int(i)**2
    return counter 
    
class Solution(object):

    def isHappy(self,n):
        counter = 0
        flag = 1
        if n == 1:
            return True
        
        while n!= 1:
            n = square(n)
            counter = counter + 1
            if counter > 10:
                flag = 0
                break
            # print (n)
            
        if flag == 0:
            return False
        else:
            return True
        
        
    
        