class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for g in range (len(nums)):
            for b in range ((g+1),len(nums)):
                if nums[g] + nums[b] == target:
                    return[g,b]