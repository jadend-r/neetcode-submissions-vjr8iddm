class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #graph cycle detection problem
        #view our prereqs as directed graph w/ edge from course -> preq
        #if a cycle exists in this graph, impossible to finish all courses

        adj = defaultdict(list)
        visited = set()
        for course, prereq in prerequisites:
            adj[course].append(prereq)

        def dfs(course):
            if course in visited:
                return False

            if adj[course] == []:
                return True

            visited.add(course)
            for prereq in adj[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            adj[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
            
