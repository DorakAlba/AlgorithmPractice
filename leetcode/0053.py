class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        starter = best = nums[0]
        for letter in nums[1:]:
            starter = max(starter+letter, letter)
            best = max(best,starter)
            return(best)

