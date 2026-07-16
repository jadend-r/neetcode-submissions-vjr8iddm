class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #brute force try every way to take courses n!
        #optimize o(n) topoligical sort
        #prereqs as a directed graph course -> prereq
        #indegree[course] += each incoming edge
        #do multisource bfs seeding our q with 0 indegree courses 
            #aka no preqreqs
        prereqs = collections.defaultdict(list)
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            prereqs[course].append(prereq)
            indegree[prereq] += 1

        q = deque()
        res = []

        # add courses that are not prereqs of anything else
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)
        
        while q:
            node = q.popleft()
            res.append(node)
            for prereq in prereqs[node]:
                indegree[prereq] -= 1
                if indegree[prereq] == 0:
                    q.append(prereq)

        return res[::-1] if len(res) == numCourses else []