class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        e_d = {}
        
        for i in range(lowLimit,highLimit +1):
            z = 0
            for j in str(i):
                # print (j)
                z = z + int(j)
            e_d[z] = e_d.get(z,0) + 1
        print (e_d)
        o_l = []
        for i in e_d.values():
            o_l.append(i)
        return (max(o_l))
            
            
            
                
        