class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = collections.defaultdict(list)
        cycle, added = set(), set()
        res = []

        for course, prereq in prerequisites:
            prereqs[course].append(prereq)

        def dfs(course):
            if course in added:
                return True

            if course in cycle:
                return False

            cycle.add(course)
            for prereq in prereqs[course]:
                if not dfs(prereq):
                    return False
            cycle.remove(course)
            res.append(course)
            added.add(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return res