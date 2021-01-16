'''
TWO SUM
The problem: https://leetcode.com/problems/two-sum/
'''


''' 
Solution 1: Brute force
Runtime: 48 ms
Memory Usage: 14.3 MB
Time complexity: O(n^2)
Space complexity: O(1)
'''
for i, inum in enumerate(nums):
	for j, jnum in enumerate(nums[i+1:], i+1):
		if(inum + jnum == target): return list((i, j))


'''
Solution 2: Two-pass hash table solution
Runtime: 44 ms
Memory Usage: 14.5 MB
Time complexity: O(n), 
Space complexity: O(n)
'''
hasht = {num:i for i, num in enumerate(nums)}        
for i, num in enumerate(nums):
	complement = target - num
	if (complement in hasht) and (hasht[complement] != i):
		return list((i, hasht[complement]))