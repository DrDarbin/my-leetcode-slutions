'''
1662. Check If Two String Arrays are Equivalent
Difficulty: Easy
https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
'''

'''
Solution 1 with string concatenations
Time complexity: O(n)
Space complexity: O(n)
'''

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        super_word1, super_word2 = str(), str()
        
        for w1 in word1:
            super_word1 += w1
        
        for w2 in word2:
            super_word2 += w2
        
        return  super_word1 == super_word2


'''
Solution 2 with generators
Time complexity: O(min(m, n))
Space complexity: O(1)
'''
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        def letter_generator(words):
            for word in words:
                for letter in word:
                    yield letter

        for letter1, letter2 in zip_longest(letter_generator(word1), letter_generator(word2)):
            if letter1 != letter2: return False
        return True