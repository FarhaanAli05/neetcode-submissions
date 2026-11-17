class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool

        dp components:
        - state
        dp[i]: if the word can be segmented by words in wordDict until that number. input is length of s.
        - base case
        dp[0] = true, rest of dp is false
        - recurrence
        if dp[i-len(word)] is true for word in wordDict and s[i-len(word):i] matches word, then dp[i] = True
        - computation order
        iterate from i=1 to len(s)
        - final answer
        dp[len(s) or -1] = if it can consist of words in wordDict
        """
        # dp = [True, False, False, False, True, False, False, False, False]
        # --- i = 4
        # word = leet
        # if dp[4-4] = True - yes - and s[0:4] == word: dp[4] = True
        # word = code
        # pass
        # --- i = 5
        # word = leet
        # if dp[1]
        # ...
        # --- i = 8
        # word = leet
        # if dp[4] and s[4:8] == code
        # pass
        # word = code
        # if dp[8] and s[4:8] == code, dp[8] = True
        # tc: o(s*w*s)
        # sc: o(s)

        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for word in wordDict:
                if len(word) <= i:
                    if dp[i-len(word)] and s[i-len(word):i] == word:
                        dp[i] = True
                        break
        return dp[len(s)]