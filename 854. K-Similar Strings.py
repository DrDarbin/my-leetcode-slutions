'''
854. K-Similar Strings
Difficulty: Hard
https://leetcode.com/problems/k-similar-strings/
'''

'''
Solution 1: Breadth-first search algorithm for the all possible combinations of swaps
Time complexity: O(n^2)
Space complexity: 

Status: Time Limit Exceeded
'''

class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        from collections import deque
        
        if A == B: return 0
        if len(A) == 2: return 1
        
        def get_children_nodes(A, depth):
            A = list(A)
            children_queue = deque()
            
            for i in range(len(A)):
                for j in range(i+1, len(A)):
                    S = A.copy()
                    
                    s = S[i]
                    
                    S[i] = S[j]
                    S[j] = s
                    
                    string = "".join(S)
                    children_queue += [(string, depth)]
            
            return children_queue
        
        depth = 0
        checked = []
        queue = deque()
        queue += [(A, depth)]
        
        counter = 0
        while queue:
            counter += 1
            print(counter)
            item = queue.popleft()
            if not item in checked:
                print(item)
                if item[0] == B: 
                    return item[1]
                else:
                    depth = item[1] + 1
                    queue += get_children_nodes(item[0], depth)
                    checked.append(item[0])
        
        return None