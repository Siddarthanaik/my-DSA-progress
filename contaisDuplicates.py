"""
Problem: Contains Duplicates
Platform: NeetCode 
Approach: Arrays
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort() 
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return True 
        return False 
    
