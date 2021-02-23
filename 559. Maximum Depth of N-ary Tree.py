'''
559. Maximum Depth of N-ary Tree
Difficulty: Easy
https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
'''

'''
Solution 1: Breadth-first search solution
Time complexity: O(n)
'''

'''
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
'''

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        
        from collections import deque
        queue = deque()
        
        depth = 1
        queue.append((root, depth))
        
        while queue:
            node, depth = queue.popleft()
            if node.children:
                for child in node.children:
                    queue.append((child, depth+1))
        
        return depth
        