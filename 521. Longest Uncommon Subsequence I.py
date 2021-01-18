'''
521. Longest Uncommon Subsequence I
Difficulty: Easy
https://leetcode.com/problems/longest-uncommon-subsequence-i/
'''

''' 
Solution: simple approach
Time complexity: O(min(m,n)), m,n - length of the strings respectively
Space complexity: O(1)
'''
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b: 
            return -1
        else:
            if len(a) == len(b): 
                return len(a)
            else: 
                return max(len(a), len(b))