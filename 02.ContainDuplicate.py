# ===========================================
# Problem No.: 217
# Problem Name: Contains Duplicate
# Difficulty: Easy
# Topic: Array, Hash Set
# Language: Python
# Time Complexity: O(n)
# Space Complexity: O(n)
# Date Solved: 10 July 2026
# ===========================================

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
