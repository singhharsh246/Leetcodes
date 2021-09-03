class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = len(nums)//2        
        elem_dict = {}        
        if maj == 0:
            return nums[0]        
        for i in nums:
            if i not in elem_dict.keys():
                elem_dict[i] = 1
            else:             
                if elem_dict[i] + 1 > maj:
                    return i
                else:
                    elem_dict[i] += 1
