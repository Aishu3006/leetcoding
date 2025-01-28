class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for ind in range(len(nums)):
            diff = target - nums[ind]
            if diff in hashMap:

                return [hashMap[diff], ind]
            
            hashMap[nums[ind]] = ind
            
        
        
        