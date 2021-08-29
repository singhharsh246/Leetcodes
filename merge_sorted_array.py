/*
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
*/




class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m, len(nums1)):
            print("here2")
            nums1.pop()
        if len(nums1) == 0:
            print("here")
            nums1.extend(nums2)                
        elif len(nums1) > 0 and len(nums2) > 0:
            flag1 = 0
            flag2 = 0           
            while flag1 < len(nums1) and flag2 < len(nums2):
                try:                    
                    if nums1[flag1] >= nums2[flag2]:
                        nums1.insert(flag1, nums2[flag2])
                        flag2 = flag2 + 1
                        flag1 = flag1 + 1
                    if nums1[flag1] < nums2[flag2]:
                        flag1 = flag1 + 1                        
                except:
                    break    
            nums1.extend(nums2[flag2::])
