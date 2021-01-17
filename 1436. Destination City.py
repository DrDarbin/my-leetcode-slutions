'''
1436. Destination City
Difficulty: Easy
https://leetcode.com/problems/destination-city/
'''

'''
Solution 1 with Set
Time complexity: O(n)
Space complexity: O(1)
'''
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        city_from = set(city[0] for city in paths)
        city_to = set(city[1] for city in paths)
        for city in city_to:
            if city not in city_from: return city


'''
Solution 2 with Dictionary
Time complexity: O(n)
Space complexity: O(1)
'''
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        city_from = {}
        city_to = {}
        
        for city in paths: 
            city_from.update({city[0]: 1}) 
            city_to.update({city[1]: 1})
        
        for city in city_to:
            if city not in city_from: return city