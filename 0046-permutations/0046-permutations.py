class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        if len(nums)==1:
            return [nums[:]] #Deep copy is created so that when copy is modified, original won't. 
        
        for i in range(len(nums)):
            n = nums.pop(0) # n = 1, 2, 3 nums = [2,3], [3,1], [1,2]
            perms = self.permute(nums)
            
            for perm in perms:
                perm.append(n)
                
            res.extend(perms)
            nums.append(n) 
            
        return res
            