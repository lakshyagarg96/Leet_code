class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        moves_list = []
        for i in moves:
            if i == 'U':
                moves_list.append(10000)
            elif i =='D':
                moves_list.append(-10000)
            elif i =='L':
                moves_list.append(1)
            elif i =='R':
                moves_list.append(-1)
        if sum(moves_list) == 0:
            return True
            
                
        