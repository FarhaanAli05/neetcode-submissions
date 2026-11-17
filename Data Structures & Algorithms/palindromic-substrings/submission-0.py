class Solution:
    def countSubstrings(self, s: str) -> int:
        # iterate through the string checking for even and odd length palindromes
        # do odd and even-length palindrome checks. for each palindrome found, increase the palindrome count by 1
        # palindrome logic: step through string with for loop. inner while loop checks if the left and right pointers are in bounds and are equal letters. while true, decrement left and increment right. do the same for even-length palindromes. maintain a total variable

        # tc: o(n^2)
        # sc: o(1)

        total = 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                total += 1
                l -= 1
                r += 1
        for i in range(len(s)):
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                total += 1
                l -= 1
                r += 1
        return total