class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_dict = {}
        for s in strs:
            chars = [0] * 26
            for c in s:
                chars[ord(c) - ord('a')] += 1
            key = tuple(chars)
            if key in freq_dict:
                freq_dict[key].append(s)
            else:
                freq_dict[key] = [s]
        return list(freq_dict.values())