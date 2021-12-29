class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        # prices = [10,1,1,6]
        o_l = []
        for i in range(len(prices)):
            discount = 0
            a = prices[i]
            for j in range(i+1,len(prices)):
                if a >= prices[j]:
                    discount = prices[j]
                    final_price = a - discount
                    # print (a,discount)
                    o_l.append(final_price)
                    break
                if j == len(prices)-1 and discount == 0:
                    final_price = a
                    o_l.append(final_price)
        o_l.append(prices[-1])
        return o_l
            
        