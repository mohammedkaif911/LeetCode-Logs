class Solution:
    def maxArea(self, height: List[int]) -> int:
        right_ptr = len(height) - 1
        left_ptr = 0
        max_area = 0
        while (left_ptr < right_ptr):
            if height[left_ptr] < height[right_ptr]:
                area = (right_ptr - left_ptr) * height[left_ptr]
                if area > max_area:
                    max_area = area
                left_ptr +=1
            else:
                area = (right_ptr - left_ptr) * height[right_ptr]
                if area > max_area:
                    max_area = area
                right_ptr -=1
        return max_area

        