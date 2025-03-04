class Solution:
    def getCombinations(self, routes, combinationSize):
        combinations = []

        def dfs(startInd, currentCombination):
            if len(currentCombination)==combinationSize:
                combinations.append(tuple(currentCombination))
                return
            
            if startInd>=len(routes):
                return
            
            #Take
            currentCombination.append(routes[startInd])
            dfs(startInd+1, currentCombination)

            #Not Take
            currentCombination.pop()
            dfs(startInd+1, currentCombination)

        dfs(0, [])
        return combinations

    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        userRoutes = defaultdict(list)
        for time, user, site in sorted(zip(timestamp, username, website)):
            userRoutes[user].append(site)
        print(userRoutes)
        
        webRouteFreqMap = defaultdict(int)
        for user, webRoutes in userRoutes.items():
            routeCombinations = set(self.getCombinations(webRoutes, 3))
            for webRoute in routeCombinations:
                webRouteFreqMap[webRoute] += 1
        print(webRouteFreqMap)
        
        maxVal = max(webRouteFreqMap.values())
        routes = []
        for route, freq in webRouteFreqMap.items():
            if freq==maxVal:
                routes.append(route)
        
        if len(routes)>1:
            routes.sort()
        
        return routes[0]

        

        