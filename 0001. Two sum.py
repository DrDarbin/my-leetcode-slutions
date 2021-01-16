'''
1. Two Sum
Difficulty: Easy
https://leetcode.com/problems/two-sum/
'''

''' 
Solution 1: Brute force
Time complexity: O(n^2)
Space complexity: O(1)
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
		for i, inum in enumerate(nums):
			for j, jnum in enumerate(nums[i+1:], i+1):
				if(inum + jnum == target): return list((i, j))


'''
Solution 2: Two-pass hash table solution
Time complexity: O(n), 
Space complexity: O(n)
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
		hasht = {num:i for i, num in enumerate(nums)}        
		for i, num in enumerate(nums):
			complement = target - num
			if (complement in hasht) and (hasht[complement] != i):
				return list((i, hasht[complement]))


'''
Solution 3: One-pass hash table solution
Time complexity: O(n), 
Space complexity: O(n)
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
		hasht = {}
		for i, num in enumerate(nums):
			complement = target - num
			if (complement in hasht) and (hasht[complement] != i):
				return list((i, hasht[complement]))
			hasht[num] = i