'''
521. Longest Uncommon Subsequence I
Difficulty: Easy
https://leetcode.com/problems/arranging-coins/
'''

''' 
Solution 1: math approach
Time complexity: O(1)
Space complexity: O(1)

Stages are an arithmetic progression, so
Sum of stages = s*(s+1)/2, where s is the number of stages
it should be equal to some m = n + x, where x is the remainder
The equasion is solved with the help of the square roots
'''
class Solution:
    def arrangeCoins(self, n: int) -> int:
        while True:
            if n == 0: return 0
            stages = -0.5 + math.sqrt(0.25 + 2*n)
            return math.floor(stages)