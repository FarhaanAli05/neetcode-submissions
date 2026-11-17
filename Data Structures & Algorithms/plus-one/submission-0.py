class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        total = 0
        length = len(digits)
        for i in range(0, length):
            total += digits[i] * 10 ** (length - 1 - i)
        total += 1
        str_total = str(total)
        new_digits = []
        for i in str_total:
            new_digits.append(int(i))
        return new_digits