class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        water = 0
        max_l = 0
        max_r = 0
        while l <= r:
            if max_l < max_r:
                w = max_l - height[l]
                if w >= 0:
                    water += w
                max_l = max(max_l, height[l])
                l += 1
            else:
                w = max_r - height[r]
                if w >= 0:
                    water += w
                max_r = max(max_r, height[r])
                r -= 1
        return water