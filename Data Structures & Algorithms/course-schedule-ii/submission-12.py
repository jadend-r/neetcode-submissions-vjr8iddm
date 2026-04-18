class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = collections.defaultdict(list)
        for course, prereq in prerequisites:
            prereqs[course].append(prereq)
        res = []
        visited = set()
        added = set()

        def dfs(course):
            if course in visited:
                return False
            if course in added:
                return True

            visited.add(course)
            added.add(course)
            for prereq in prereqs[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            res.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                print("false", course)
                return []

        return res