# ===========================================
# Problem No.   : 1
# Problem Name  : Two Sum
# Difficulty    : Easy
# Topic         : Array, Hash Table
# Language      : Python
# Approach      : Brute Force (Nested Loops)
# Time Complexity  : O(n²)
# Space Complexity : O(1)
# Date Solved   : 9 July 2026
# ===========================================

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return i,j
