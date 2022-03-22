class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        o_l = []
        for i in range(len(candies)):
            candies_second_copy = candies.copy()
            candies_second_copy[i] = candies_second_copy[i] + extraCandies
            candies_copy = candies_second_copy.copy()
            a = candies_second_copy[i]
            candies_copy.remove(a)
            b = max(candies_copy)
            # print (a,b,candies_second_copy)
            if a >= b:
                o_l.append(True)
            else:
                o_l.append(False)
        return (o_l)
        