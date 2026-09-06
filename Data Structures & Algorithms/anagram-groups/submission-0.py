class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #use hashmap keyed {counts}: [words]
            #for every str, count chars o(n * L), use as key to hm
            #O(n) space

        groups = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - 97] += 1
            groups[tuple(count)].append(s)

        return list(groups.values())