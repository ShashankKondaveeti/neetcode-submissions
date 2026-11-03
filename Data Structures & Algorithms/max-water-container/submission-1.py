class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0
        l = 0
        r = len(heights) - 1
        while l != r:
            l_height = heights[l]
            r_height = heights[r]
            curr_area = min(l_height, r_height) * (r - l)
            if curr_area > largest:
                largest = curr_area
            if l_height < r_height:
                l += 1
            else:
                r -= 1
        return largest


            