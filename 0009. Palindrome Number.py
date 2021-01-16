'''
9. Palindrome Number
Difficulty: Easy
https://leetcode.com/problems/palindrome-number/

Time complexity: O(lg(n))
Space complexity: O(1)
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        import math
        
        if (x < 0 or (x % 10 == 0 and x != 0)): return False
        
        # reverted last part of the number
        z = 0
        while (x > z):
            z = z * 10 +  x % 10
            x = math.floor(x / 10)
        
        # for an odd number we can just skip the central digit
        return x == z or x == math.floor(z / 10)