class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = collections.defaultdict(list)
        visited = set()
        added = set()
        res = []

        for course, prereq in prerequisites:
            prereqs[course].append(prereq)

        def dfs(course):
            if prereqs[course] == []:
                if course not in added:
                    res.append(course)
                    added.add(course)
                return True

            if course in visited:
                return False

            visited.add(course)
            for prereq in prereqs[course]:
                if not dfs(prereq):
                    return False
            prereqs[course] = []
            visited.remove(course)
            res.append(course)
            added.add(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return res