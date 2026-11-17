class Solution(object):
    from collections import defaultdict
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = defaultdict(list)
        for s in strs:
            chars = [0] * 26
            for c in s:
                chars[ord(c) - ord('a')] += 1
            key = tuple(chars)
            anagrams[key].append(s)
        return list(anagrams.values())