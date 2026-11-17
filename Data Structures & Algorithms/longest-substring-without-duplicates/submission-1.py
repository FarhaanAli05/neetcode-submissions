class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        n = len(s)
        sett = set()
        max_sub = 0
        for r in range(n):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1
            sett.add(s[r])
            max_sub = max(max_sub, (r - l) + 1)
        return max_sub