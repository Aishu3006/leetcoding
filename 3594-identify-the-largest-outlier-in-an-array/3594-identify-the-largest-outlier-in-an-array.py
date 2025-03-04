class Solution:
    '''
    def getCombinations(self, nums):
        combinations = []

        def dfs(ind, currentCombination):
            if len(currentCombination)==2:
                combinations.append(currentCombination.copy())
                return
            
            if ind>=len(nums):
                return 

            #Take
            currentCombination.append(nums[ind])
            dfs(ind+1, currentCombination)

            #Not Take
            currentCombination.pop()
            dfs(ind+1, currentCombination)

        dfs(0,[])
        return combinations

    def getLargestOutlier(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        combinations = self.getCombinations(nums)

        outlier = float("-inf")
        for A,B in combinations:
            val = totalSum - A - B
            if val==A:
                outlier = max(outlier, B)
            elif val==B:
                outlier = max(outlier, A)
            else:
                continue
        
        return outlier
        '''
    def getLargestOutlier(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        numCount = defaultdict(int)
        for num in nums:
            numCount[num] += 1
        
        largestOutlier = float("-inf")

        #Considering each num can be the sum in [sum, outlier]
        # TotalSum = 2*sum + outlier
        for num in nums:
            potentialOutlier = totalSum - 2*num

            if potentialOutlier in numCount:
                if potentialOutlier!=num or numCount[num]>1:
                    largestOutlier = max(largestOutlier, potentialOutlier)
            
        return largestOutlier


        