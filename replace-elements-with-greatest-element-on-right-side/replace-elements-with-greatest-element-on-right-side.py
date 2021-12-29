class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        o_l = []
        for i in range(len(arr)-1):
            a = arr[i]
            b = max (arr[i+1:])
            o_l.append(b)
        o_l.append(-1)
        return o_l
                
            
        