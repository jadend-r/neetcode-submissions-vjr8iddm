class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #brute force try every way to take courses O(n! * (V+E))
        #optimize to O(V+E) topoligical sort
        #prereqs as a directed graph course -> prereq
        #indegree[course] += each incoming edge
        #do multisource bfs seeding our q with 0 indegree courses 
            #aka no preqreqs
        #numCourses = V #preqresuisites = E
        prereqs = collections.defaultdict(list)
        indegree = [0] * numCourses
        
        #O(E)
        for course, prereq in prerequisites:
            prereqs[course].append(prereq)
            indegree[prereq] += 1

        q = deque()
        res = []

        # add courses that are not prereqs of anything else
        #O(V)
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)
        
        while q: #O(V)
            node = q.popleft()
            res.append(node)
            for prereq in prereqs[node]: #O(E)
                indegree[prereq] -= 1
                if indegree[prereq] == 0:
                    q.append(prereq)
        #O(V+E) total time 

        return res[::-1] if len(res) == numCourses else []