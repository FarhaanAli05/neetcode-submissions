class Solution:
    def longestPalindrome(self, s: str) -> str:
        # logic: start two pointers at centre of string
        # record that as the largest palindrome and record its length
        # expand the left and right pointers outward and on each expansion, check: are the letters still equal (while loop)? is my string length greater than the previous strLen val (if condition)? are my pointers in bounds (while loop)?
        # if all of the above are true, record the new palindrome length and the new palindrome
        # if the if condition fails, simply increment/decrement the pointers
        # if the while loop condition fails, break and return res
        # tc: o(n^2) - expansion outward for each letter in s, sc: o(1)

        # test case - s = "babad"
        # res = "b", resLen = 1, len(s) = 5
        # --- i = 0, l = 0, r = 0
        # l, r = 0, 0
        # b = b
        # 1 > 0
        # resLen = 1
            # l = 1, r = -1 BREAK
        # --- i = 1
        # l, r = 1, 1
        # a = a
        # resLen = 1, res = "b"
        # l = 0, r = 2
            # 3 > 1
            # res = "bab"
            # l = -1, r = 3 BREAK
        res = ""
        resLen = 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    res = s[l:r+1]
                l -= 1
                r += 1
        for i in range(len(s)):
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = (r - l + 1)
                    res = s[l:r+1]
                l -= 1
                r += 1
        return res