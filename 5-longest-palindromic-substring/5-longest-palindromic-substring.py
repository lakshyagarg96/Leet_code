class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Brute force approach will result in time limit exceed
        # e_s = ""
        # len_counter = 0
        # for i in range(len(s)):
        #     for j in range(len(s)):
        #         start = s[i]
        #         if j >= i:
        #             forward_string = s[i:j+1]
        #             backward_string = forward_string[::-1]
        #             # print  ("forward string:",forward_string)
        #             # print ("Backward string:",backward_string)
        #             if forward_string == backward_string:
        #                 if len(forward_string) > len_counter:
        #                     e_s = forward_string
        #                     len_counter = len(forward_string)
        # # print (e_s)
        # return e_s
        # # return forward_string, backward_string
        
        # Two pointer approach
        e_s = ""
        len_counter = 0
        for i in range(len(s)):
            # to find odd length palindromes we xan use this approach 
            left_pointer = i
            right_pointer = i
            while (left_pointer >= 0 and right_pointer <= len(s)-1) and (s[left_pointer] == s[right_pointer]):
                # print (s[left_pointer:right_pointer+1])
                if len(s[left_pointer:right_pointer+1]) > len_counter:
                    e_s = s[left_pointer:right_pointer+1]
                    len_counter = len(s[left_pointer:right_pointer+1])
                    # print (e_s)
                left_pointer -= 1
                right_pointer += 1
            # to find even length palindromes we change the value of right_pointer to i+1 to  use this approach 
            # else he code remains the same as above
            left_pointer = i
            right_pointer = i+1
            while (left_pointer >= 0 and right_pointer <= len(s)-1) and (s[left_pointer] == s[right_pointer]):
                # print (s[left_pointer:right_pointer+1])
                if len(s[left_pointer:right_pointer+1]) > len_counter:
                    e_s = s[left_pointer:right_pointer+1]
                    len_counter = len(s[left_pointer:right_pointer+1])
                    # print (e_s)
                left_pointer -= 1
                right_pointer += 1
        return e_s
                    
        
            

        