class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)
        
        for n, fre in count.items():
            freq[fre].append(n)
        
        res = []
        for i in range(len(freq)-1, -1, -1):
            for ele in freq[i]:
                res.append(ele)

                if len(res)==k:
                    return res
            
        
        
        
        