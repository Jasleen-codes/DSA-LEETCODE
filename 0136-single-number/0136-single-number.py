class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        results=0
        for num in nums:
            results = results^num
        return results

        