class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = collections.defaultdict(list)
        visited = set()
        # build the adjacency list
        for course, prereq in prerequisites:
            prereqs[course].append(prereq)

        def dfs(course):
            if prereqs[course] == []: #No prereqs, course can complete
                return True
            if course in visited: #Cycle exists, cant complete
                return False
            
            visited.add(course)
            for prereq in prereqs[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

            