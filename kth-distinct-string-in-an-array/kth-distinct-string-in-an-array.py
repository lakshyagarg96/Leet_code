class Solution:
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        e_d = {}
        for i in arr:
            e_d[i] = e_d.get(i, 0) + 1
        o_l = []
        for z,v in e_d.items():
            if v == 1:
                o_l.append(z)
        if k > len(o_l):
            return ''
        else:
            return o_l[int(k)-1]
                
        