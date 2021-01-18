'''
344. Reverse String
Difficulty: Easy
https://leetcode.com/problems/reverse-string/
'''

'''
Solution 1 with pointers
Time complexity: O(n)
Space complexity: O(1)
'''

class Solution:
    def reverseString(self, s: List[str]) -> None:      
        center = math.floor(len(s)/2)
        for i in range(0, center):            
            first = s[i]
            last = s[len(s) - 1 - i]
            s[i] = last
            s[len(s) - 1 - i] = first