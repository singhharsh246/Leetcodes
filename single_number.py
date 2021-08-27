"""

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.


"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        elem = nums[0]
        for i in range(1, len(nums) - 1):
            try:
                if nums[i] != nums[i+1] and nums[i] != nums[i-1]:
                    elem = nums[i]
            except:
                break
        if len(nums) > 2:
            if nums[len(nums) - 1] != nums[len(nums) - 2]:
                elem = nums[len(nums) - 1]
        return elem