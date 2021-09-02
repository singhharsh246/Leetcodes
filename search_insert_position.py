class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        low = 0
        high = len(nums)
        mid = ( low + high )//2
              
        while True:            
            if target == nums[mid]:
                return mid            
            elif low == mid:
                if target >= nums[mid]:
                    return mid+1
                else:
                    return mid
            elif target > nums[mid]:               
                low = mid
                mid = ( low + high )//2           
            elif target < nums[mid]:
                high = mid
                mid = ( low + high )//2
