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


'''
Solution 2: Breadth-first search algorithm without unneccesary letters swaps
Solution with comments

Time complexity:
Space complexity: 

Status: Time Limit Exceeded
'''
class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        from collections import deque
        
        # if there is only one element or A = B
        if A == B: return 0
        
        def get_children_nodes(A):
            # let A be unchangable
            S = list(A).copy()
            
            # go through the all S letters and create all appropriate swaps
            for i in range(len(S)):
                # if innitial letters for A and B are the same, 
                # than we do not need unneccessary swaps
                if S[i] != B[i]: 
                    # let's find a letter to make a swap with
                    for j in range(i+1, len(S)):
                        # if the new letter in S equals B-letter at the same possition
                        # than we do not need unneccessary swaps again
                        if (S[j] == B[i]) and (S[j] != B[j]):
                            # swap the elements and yield a new word for a generator
                            S[i], S[j] = S[j], S[i]
                            yield "".join(S)
                            
                            # swap the letters back in order to continue creating
                            # the combinations
                            S[i], S[j] = S[j], S[i]
                        else: 
                            continue
                else: 
                    continue
        
        # Breadth-first search algorithm
        # create a queue and initial state
        queue = deque()
        queue += [A]
        check_depth = {A: 0}
        
        # check the queue items one by one and add new children elements to the queue
        while queue:
            parent = queue.popleft()
            # correct match
            if parent == B: 
                return check_depth[parent]
            # possible valid child swap combinations for the current parent element
            else:
                for child in get_children_nodes(parent):
                    if child not in check_depth:
                        check_depth[child] = check_depth[parent]+1
                        queue += [child]
        
        return None