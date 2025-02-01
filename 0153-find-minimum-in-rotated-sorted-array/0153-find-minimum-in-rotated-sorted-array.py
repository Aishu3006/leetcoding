class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==0:
            return nums[0]
        
        l = 0
        r = len(nums)-1
        curMin = nums[l]
        while l<r:
            m = l + (r-l)//2
            curMin = min(curMin, nums[m])
            if nums[m]>nums[r]:
                l = m+1
            else:
                r = m - 1
        
        return min(curMin, nums[l])

                
            