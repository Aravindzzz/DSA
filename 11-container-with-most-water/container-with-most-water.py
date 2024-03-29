class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, ans, right = 0, 0, len(height) - 1
        while left < right:
            ans = max(ans, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans

        