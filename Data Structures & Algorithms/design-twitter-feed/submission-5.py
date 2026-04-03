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
                mostRecent = len(self.posts[followeeId]) - 1
                count, tweetId = self.posts[followeeId][mostRecent]
                maxHeap.append([count, tweetId, followeeId, mostRecent - 1])
        heapq.heapify_max(maxHeap)
        while maxHeap and len(res) < 10:
            _, tweetId, followeeId, nxtTweetIndx = heapq.heappop_max(maxHeap)
            res.append(tweetId)
            if nxtTweetIndx >= 0:
                count, tweetId = self.posts[followeeId][nxtTweetIndx]
                heapq.heappush_max(maxHeap, [count, tweetId, followeeId, nxtTweetIndx - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
