class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Kahn's algorithm
        indegree = [0]*numCourses
        prereqMap = defaultdict(list)
        q = deque()

        for crs, prereq in prerequisites:
            indegree[crs] += 1
            prereqMap[prereq].append(crs)
        
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        
        coursesTaken = 0
        while q:
            course = q.popleft()
            coursesTaken += 1

            for crs in prereqMap[course]:
                indegree[crs] -= 1

                if indegree[crs]==0:
                    q.append(crs)
        
        return numCourses==coursesTaken



        '''
        courseMap = defaultdict(list)

        for crs, prereq in prerequisites:
            courseMap[crs].append(prereq)

        completed = set()
        visiting = set()

        def checkCourse(course):
            if course in completed:
                return True
            
            if course in visiting:
                return False
            
            visiting.add(course)

            for prereq in courseMap[course]:
                if not checkCourse(prereq):
                    return False
            
            visiting.remove(course)
            completed.add(course)

            return True
        
        for crs in range(numCourses):
            if not checkCourse(crs):
                return False
        
        return True
        '''
        