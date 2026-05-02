class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        for course, prereq in prerequisites:
            adj[course].append(prereq)

        res = []
        visited = set()
        added = set()

        def dfs(course):
            if course in visited:
                print("ret false", course)
                return False

            if course in added:
                return True

            visited.add(course)
            for prereq in adj[course]:
                if not dfs(prereq):
                    print("ret false", course, prereq)
                    return False
            visited.remove(course)
            adj[course] = []
            res.append(course)
            added.add(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                print("ret false ok", course)
                return []

        print("yuh")
        return res