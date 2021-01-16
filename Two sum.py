''' 
Brute force
Runtime: 48 ms
Memory Usage: 14.3 MB
Time complexity: O(n^2), 
Space complexity: O(1)
'''
for i, inum in enumerate(nums):
	for j, jnum in enumerate(nums[i+1:], i+1):
		if(inum + jnum == target): return list((i, j))