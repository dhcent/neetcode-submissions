class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Run a prefix suffix idea: 
        # Have a stack and:
        # prior to adding an item, if that item is smaller than the current top stack. pop the top 
        # (max width from that chosen height)
        # Then add the item
        # have a concurrent stack running to determine leftwards. if that item si smaller than curr
        # top, pop the top
        # res_L, res_R
        # res stores LOCATIONS of right bounds for each rect. idx to right bound
        res_L = [-1] * len(heights)
        res_R = [-1] * len(heights)
        stack_L = []
        stack_R = []
        for i in range(len(heights)):
            j = len(heights) - 1 - i #iterate from right to left
            R_h = heights[i]
            L_h = heights[j]
            if i == 0:
                stack_L.append([L_h, j])
                stack_R.append([R_h, i])
                continue
            # keep popping until stack_R is empty or the height is no longer less. 
            while stack_R and R_h < stack_R[-1][0]:
                res_R[stack_R.pop()[1]] = i - 1

            while stack_L and L_h < stack_L[-1][0]:
                res_L[stack_L.pop()[1]] = j + 1

            stack_L.append([L_h, j])
            stack_R.append([R_h, i])

        for i in range(len(res_R)):
            if res_R[i] == -1:
                res_R[i] = len(res_R) - 1 #index of right bound.
            if res_L[i] == -1:
                res_L[i] = 0
        widths = [r - l + 1 for r,l in zip(res_R, res_L)]
        areas = [l * w for l,w in zip(heights, widths)]
        return max(areas)






