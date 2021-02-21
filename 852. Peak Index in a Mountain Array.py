'''
852. Peak Index in a Mountain Array
Difficulty: Easy
https://leetcode.com/problems/peak-index-in-a-mountain-array/

Solution 1: Binary search
Time complexity: O(log n)
Space complexity: O(1)
'''
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low = 0
        high = len(arr) - 1

        while True:
            # since the array is not one way sorted the tip can be found on the edges during the implementation of the binary search algorithm
            if len(arr[low:high+1]) == 2:
                if arr[low] > arr[high]: 
                    return low
                else:
                    return high
            
            mid = (low + high) // 2

            # the tip
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            
            # left side of the mountain
            if arr[mid] < arr[mid+1]:
                low = mid+1
            
            # right side of the mountain
            if arr[mid] < arr[mid-1]:
                high = mid
            
        return None