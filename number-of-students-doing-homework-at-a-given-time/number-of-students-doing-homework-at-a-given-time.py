class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        counter = 0
        for i in range(len(startTime)):
            a = startTime[i]
            b = endTime[i]
            if queryTime >= a and queryTime <= b:
                counter += 1
            
        return counter
                    
        