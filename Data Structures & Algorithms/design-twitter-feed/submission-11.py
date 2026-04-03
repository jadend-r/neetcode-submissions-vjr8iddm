class Twitter:

    def __init__(self):
        self.count = 0
        self.posts = collections.defaultdict(list) # userId: maxHeap
        self.following = collections.defaultdict(set) #userId: [following]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append([self.count, tweetId])
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        res = []
        self.following[userId].add(userId)
        for followeeId in self.following[userId]:
            if followeeId in self.posts:
                last = len(self.posts[followeeId]) - 1
                count, tweetId = self.posts[followeeId][last]
                maxHeap.append([count, tweetId, followeeId, last - 1])
        heapq.heapify_max(maxHeap)
        while maxHeap and len(res) < 10:
            count, tweetId, followeeId, last = heapq.heappop_max(maxHeap)
            res.append(tweetId)   
            if last >= 0:
                count, tweetId = self.posts[followeeId][last]
                heapq.heappush_max(maxHeap, [count, tweetId, followeeId, last - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
