class Solution(object):
    def maxProfit(self, prices):
        
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = float('inf')
        profit = float('-inf')
        
        for idx, price in enumerate(prices):
            buy = min(buy, price)
            profit = max(profit, price - buy)
        return profit
        
        # Pointer based approach
#         max_profit = 0
#         i = 0
#         for i in range(len(prices)):
#             left = i
#             right =len(prices) - 1
            # Checks the condition that stock cannot be sold efore buying it
#             while right > left:
#                 profit = prices[right] - prices[left]
                
#                 if profit > max_profit:
#                     max_profit = profit
#                 else:
#                     max_profit = max_profit
#                 right -= 1
        
#         return max_profit
                
            
            
        # brute force
#         compare = 0
#         for i in range(0,len(prices)):
#             for j in prices[i+1:]:
#                 print (prices[i],j)
#                 counter = j - prices[i]
#                 if counter > compare:
#                     compare = counter
                    
#         return (compare)

       
    
    
    
    
    

         
        