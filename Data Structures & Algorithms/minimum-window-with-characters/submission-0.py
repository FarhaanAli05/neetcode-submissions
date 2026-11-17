class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        n = len(s)
        l = 0
        count_t, count_win = {}, {}
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1
        need, have = len(count_t), 0
        res, res_len = [-1, -1], float('inf')

        for r in range(n):
            c = s[r]
            count_win[c] = count_win.get(c, 0) + 1
            if c in count_t and count_t[c] == count_win[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < res_len:
                    res_len = r - l + 1
                    res = [l, r]
                count_win[s[l]] -= 1
                if s[l] in count_t and count_t[s[l]] > count_win[s[l]]:
                    have -= 1
                l += 1
        l, r = res

        return s[l:r+1] if res_len != float('inf') else ""