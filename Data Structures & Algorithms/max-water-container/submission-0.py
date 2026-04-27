class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxArea = 0

        for i in range(len(heights)):
            # Ensure left has not passed right
            if left < right:
                area = min(heights[left], heights[right]) * (right - left)
                maxArea = max(area, maxArea)

                # Move the pointers appropriately
                if heights[left] < heights[right]:
                    left += 1
                elif heights[left] > heights[right]:
                    right -= 1
                elif heights[left] == heights[right]:
                    left += 1
                    right -= 1

            else:
                break
        
        return maxArea
