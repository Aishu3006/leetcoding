class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            hashset.add(n)
        
        return len(hashset)!=len(nums)