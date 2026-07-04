class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 2 pointers: one on left and one on right
        # Determine the area based on the "width" (difference between indexes * 2)
        # then move about the smaller height inwards (if left, +1, if right, -1). Idea is that:
        # if we move the bigger height, we will always get a smaller (since height 
        # is bounded by smaller one and width is increasing)
        Area = []
        L = 0
        R = len(heights) - 1

        while L < R:
            Area.append(min(heights[L], heights[R]) * (R - L))

            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1

        return max(Area)
