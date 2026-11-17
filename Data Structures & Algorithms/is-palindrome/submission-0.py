class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        arr = [char for char in s if char.isalnum()]
        for i in range(len(arr) - 1, -1, -1):
            index = len(arr) - i - 1
            if arr[i] != arr[index]:
                return False
        return True