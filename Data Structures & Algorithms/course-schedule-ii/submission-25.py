class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        adj = defaultdict(list)
        for course, prereq in prerequisites:
            adj[course].append(prereq)

        visited = set()
        added = set()
        def dfs(course):
            if course in added:
                return True
            if course in visited:
                return False
            
            visited.add(course)
            for nei in adj[course]:
                if not dfs(nei):
                    return False

            added.add(course)
            res.append(course)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return []
        return res 
            

