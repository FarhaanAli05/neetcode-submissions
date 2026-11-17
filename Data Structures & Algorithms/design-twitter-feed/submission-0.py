class Twitter:

    def __init__(self):
        """
        tc: o(1)
        sc: o(1)
        """
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.time = 0

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None

        tc: o(1)
        sc: o(1)
        """
        self.tweets[userId].append((-self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]

        tc: o(n + 10 log n), n is the number of users
        sc: o(n)
        """
        res = []
        newest_tweets = []
        users = self.following[userId]
        users.add(userId)
        for user in users:
            index = len(self.tweets[user]) - 1
            if index >= 0:
                time, tweetId = self.tweets[user][index]
                newest_tweets.append((time, tweetId, user, index - 1))
        heapq.heapify(newest_tweets)
        while newest_tweets and len(res) < 10:
            time, tweetId, user, index = heapq.heappop(newest_tweets)
            res.append(tweetId)
            if index >= 0:
                time, tweetId = self.tweets[user][index]
                heapq.heappush(newest_tweets, (time, tweetId, user, index - 1))
        return res

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None

        tc: o(1)
        sc: o(1)
        """
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None

        tc: o(1)
        sc: o(1)
        """
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)