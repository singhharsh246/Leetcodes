"""

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.



"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        target_index = list(i for i, j in enumerate(nums) if j == target)


        if len(target_index) == 0:
            return [-1, -1]

        indexes = []
        indexes.append(min(target_index))
        indexes.append(max(target_index))


        return indexes