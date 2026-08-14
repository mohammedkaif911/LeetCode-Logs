# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         max_sum = nums[0]
#         current_sum = 0
#         for n in nums:
#             current_sum = current_sum + n
#             if current_sum > max_sum:
#                 max_sum = max(max_sum ,current_sum)
#             if current_sum<0:
#                 current_sum = 0
#         return max_sum
        


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        currsum = 0
        for num in nums:
            currsum = currsum + num
            if currsum > maxsum:
                maxsum = currsum
            if currsum < 0:
                currsum = 0
        return maxsum
