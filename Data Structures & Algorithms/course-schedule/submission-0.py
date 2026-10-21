class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # we map every course to an empty list
        preMap= { i :[] for i in range(numCourses)}
        for course, pre in prerequisites:
            preMap[course].append(pre)

        #visitSet= all courses along the curr DFS path
        visitSet= set()
        def dfs(course):
            # to detect loop, this course cannot be completed, we visited it twice
            if course in visitSet:
                return False
            # this course has no prereqs
            if preMap[course]==[]:
                return True
            visitSet.add(course)
            for pre in preMap[course]:
                if not dfs(pre): return False
            visitSet.remove(course)
            preMap[course]=[]
            return True
        for course in range(numCourses):
            if not dfs(course): return False
        return True

