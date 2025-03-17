class Solution:
    def getCombinations(self, route, combinationSize):
        combinations = []

        def dfs(i, current):
            if len(current)==combinationSize:
                combinations.append(tuple(current))
                return
            
            if i>=len(route):
                return
            
            #Take
            current.append(route[i])
            dfs(i+1, current)

            #Not Take
            current.pop()
            dfs(i+1, current)

        dfs(0, [])
        return combinations
        '''
        combinations = []

        def dfs(ind, currentCombination):
            
            if len(currentCombination)==combinationSize:
                combinations.append(tuple(currentCombination))
                return
            
            if ind>=len(route):
                return
            
            #Take
            currentCombination.append(route[ind])
            dfs(ind+1, currentCombination)

            #Not Take
            currentCombination.pop()
            dfs(ind+1, currentCombination)
        
        dfs(0, [])
        print(combinations)
        return combinations
        '''

    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        userRouteMap = defaultdict(list)

        for time, user, site in sorted(zip(timestamp, username, website), key = lambda x:(x[0], x[1])):
            userRouteMap[user].append(site)
        
        patternFreqMap = defaultdict(int)
        for user, webRoutes in userRouteMap.items():
            patterns = set(self.getCombinations(webRoutes, 3))

            for pattern in patterns:
                patternFreqMap[pattern] += 1
        
        maxFreq = max(patternFreqMap.values())

        res = []
        for pattern, freq in patternFreqMap.items():
            if freq==maxFreq:
                res.append(pattern)
        
        if len(res)>1:
            res.sort()
        
        return res[0]

        '''
        userRouteMap = defaultdict(list)
        for time, user, site in sorted(zip(timestamp, username, website)):
            userRouteMap[user].append(site)
        
        patternFreqMap = defaultdict(int)
        for user, webRoute in userRouteMap.items():
            patterns = set(self.getCombinations(webRoute, 3))
            for pattern in patterns:
                patternFreqMap[pattern] += 1
        
        maxVal = max(patternFreqMap.values())
        res = []
        for pattern, freq in patternFreqMap.items():
            if patternFreqMap[pattern] == maxVal:
                res.append(pattern)
        
        if len(res)>1:
            res.sort()
        
        return res[0]
        '''

        