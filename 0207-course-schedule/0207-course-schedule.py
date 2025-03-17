class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

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
        