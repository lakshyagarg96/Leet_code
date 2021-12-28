class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        n = len(s) + 1
        values = []
        for j in range(n):
            values.append(j)
        print (values)
        
        output = []
        counter = 0
        for i in s:
            if i =='I':
                output.insert(counter,min(values))
                values.remove(min(values))
            if i == 'D':
                output.insert(counter,max(values))
                values.remove(max(values))
            counter += 1
        output.append(values[0])
        # if s[0] == 'I':
        #     output.insert(0,0)
        # else:
        #     ouput.insert(0,1)
        return (output)
            
                
                
            
        