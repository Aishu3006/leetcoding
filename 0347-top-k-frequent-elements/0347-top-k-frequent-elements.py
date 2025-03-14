class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        freqBucketList = [[] for i in range(len(nums)+1)]

        for num, freq in count.items():
            freqBucketList[freq].append(num)
        
        res = []
        for i in range(len(freqBucketList)-1, -1, -1):
            for ele in freqBucketList[i]:
                res.append(ele)
                if len(res)==k:
                    return res

            
        
        
        
        