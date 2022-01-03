class Solution:
    def checkString(self, s: str) -> bool:
        # s = 'abab'
        a_pos = -1
        b_pos = -1
        for i in range(len(s)):
            if s[i] == 'a':
                a_pos = i
        for i in range(len(s)):
            if s[i] == 'b':
                b_pos = i
                break
        print (a_pos, b_pos)
        if b_pos > a_pos:
            return True
        elif b_pos == -1 or a_pos == -1:
            return True
        
                
        
            
        