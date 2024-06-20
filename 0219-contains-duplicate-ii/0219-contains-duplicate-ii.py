class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        
        for i,n in enumerate(nums):
            if n in hashmap:
                j = hashmap[n]
                if abs(i-j) <= k:
                    return True
            hashmap[n] = i
        
        return False
        