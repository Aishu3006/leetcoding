class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        #Topological Sort

        prereqMap = defaultdict(list)
        indegree = [0]*numCourses
        q = deque()
        res = []

        for crs, prereq in prerequisites:
            prereqMap[prereq].append(crs)
            indegree[crs] += 1
        
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        
        while q:
            node = q.popleft()
            res.append(node)

            for crs in prereqMap[node]:
                indegree[crs]-=1

                if indegree[crs]==0:
                    q.append(crs)
        
        return res if len(res)==numCourses else []
        




        '''
        preMap = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            preMap[crs].append(pre)
            
        output = []
        path = set()
        visit = set()
        
        def dfs(crs):
            if crs in path:
                return False
            if crs in visit:
                return True
            
            path.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            path.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
            
        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return output
        '''
        