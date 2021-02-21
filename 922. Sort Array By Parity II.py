'''
922. Sort Array By Parity II
Difficulty: Easy
https://leetcode.com/problems/sort-array-by-parity-ii/
'''

'''
Solution 1: two pass approach with a selection sort algorithm
Time complexity: O(n)
Space complexity: O(1)
'''
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        def find_odd(A):
            for i in range(len(A)):
                remainer = A[i] % 2
                
                if remainer != 0:
                    return A[i], i
                
            return None
        
        def find_even(A):
            for i in range(len(A)):
                remainer = A[i] % 2
                
                if remainer == 0:
                    return A[i], i
                
            return None
        
        sorted_array = []
        for i in range(len(A)):
            remainer = i % 2
            
            if remainer == 0:
                num, num_i = find_even(A)
            else:
                num, num_i = find_odd(A)
            
            sorted_array.append(num)
            A.pop(num_i)
        
        return sorted_array
                