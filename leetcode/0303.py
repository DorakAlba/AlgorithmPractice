class NumArray:

    def __init__(self, nums: List[int]):
        self.NumArray = nums
        self.totals = [0]
        for element in self.NumArray:
            self.totals.append(self.totals[-1]+element)
    def sumRange(self, left: int, right: int) -> int:
        return (self.totals[right+1] - self.totals[left])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)