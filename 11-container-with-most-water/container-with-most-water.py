class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        ans = 0
        right = len(height)-1
        while left<=right:
            area = min(height[left],height[right]) * (right-left)
            ans = max(area,ans)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return ans

        