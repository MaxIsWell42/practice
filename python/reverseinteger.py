# https://leetcode.com/problems/reverse-integer/
# Given a 32-bit signed integer, reverse digits of an integer.

class Solution:
    def reverse(self, x: int) -> int:
        # Edge Case
        if x == 0:
            return 0
        
        temp = x
        rev = 0
        negative = False
        
        # Check if the number is negative. If so, return it's positive equivalent.
        if x < 0:
            negative = True
            x = -x
            
        # Go through the number and return it's reverse
        while(x > 0):
            last = x%10
            rev = rev*10 + last
            x = x // 10
            
            
        # Check if the number will overflow
        if rev > (2**31 - 1) or rev < ((2**31 - 1) * -1):
            print(rev)
            return 0
            
        # Switch it back to negative if it was
        if negative:
            return  -rev
        
        return rev
        print(rev)