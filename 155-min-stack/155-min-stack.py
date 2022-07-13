class MinStack(object):

    def __init__(self):
        # initilizing the stack object
        self.stack = []
        self.min = float('inf')
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        # as we have to keep the complexity as O(1) we will push the new value and minimum value of the stack in each push
        m = val
        if self.stack:
            m = min(m, self.stack[-1][1])
        self.stack.append([val,m])
            
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()