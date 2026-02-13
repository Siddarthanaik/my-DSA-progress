""""
Problem: Valid Anagram
Platform: NeetCode
Approach: Arrays
Time Complexity: O(n log n + m log m)
Space Complexity: O(1)

"""




class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False 
        return sorted(s) == sorted(t)
    