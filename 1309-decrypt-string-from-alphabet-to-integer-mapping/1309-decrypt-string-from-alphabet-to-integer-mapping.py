class Solution:
    def freqAlphabets(self, s: str) -> str:
        o_l = []
        i_list = []
        i = 0
        while i < len(s)-2:
            if s[i+2] == '#':
                a = s[i:i+2]
                i = i+3
            else:
                a = s[i]
                i = i+1
            o_l.append(a)
            i_list.append(i)
            
        if (max(i_list)) < len(s):
            for i in range(max(i_list), len(s)):
                o_l.append(s[i])
        print (o_l)
        d = {} 
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(26):
            d[ str(i+1)] =alpha[i]
        f_l = ''
        print (d)
        for j in o_l:
            for k in d:
                if k == j:
                    f_l += str(d[k])
        return (f_l)
        
                    
        

        