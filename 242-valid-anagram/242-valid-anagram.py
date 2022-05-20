class Solution(object):
    def isAnagram(self, s, t):
        s_d = {}
        t_d = {}
        for i in s:
            if i not in s_d:
                s_d[i] = 1
            else:
                s_d[i] = s_d[i] + 1
                
        for j in t:
            if j not in t_d:
                t_d[j] = 1
            else:
                t_d[j] = t_d[j] + 1
                
        return (t_d == s_d)
        
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        