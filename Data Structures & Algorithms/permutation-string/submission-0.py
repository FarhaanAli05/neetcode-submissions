class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        str_1 = [0] * 26
        for s in s1:
            str_1[ord(s) - ord('a')] += 1
        n = len(s1)
        r = 0
        str_2 = [0] * 26
        for r in range(n):
            str_2[ord(s2[r]) - ord('a')] += 1
        for r in range(n, len(s2)):
            if str_1 == str_2:
                return True
            str_2[ord(s2[r - n]) - ord('a')] -= 1
            str_2[ord(s2[r]) - ord('a')] += 1
        return str_1 == str_2