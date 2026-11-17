class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A
        l, r = 0, len(A) - 1
        total = len(A) + len(B)
        half = total // 2

        while True:
            m = (l + r) // 2 # mid of A
            n = half - m - 2 # last index of left partition in B

            leftA = A[m] if m >= 0 else float('-infinity')
            rightA = A[m + 1] if (m + 1) < len(A) else float('infinity')
            leftB = B[n] if n >= 0 else float('-infinity')
            rightB = B[n + 1] if (n + 1) < len(B) else float('infinity')
            if leftA <= rightB and leftB <= rightA:
                if total % 2:
                    return min(rightA, rightB)
                else:
                    return (max(leftA, leftB) * 1.0 + min(rightA, rightB)) / 2
            elif leftA > rightB:
                r = m - 1
            else:
                l = m + 1