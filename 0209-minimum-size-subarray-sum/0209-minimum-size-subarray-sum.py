class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf') # Set to infinity so any window size is smaller
        current_sum = 0
        left = 0
        
        for right in range(len(nums)):
            # 1. Expand the window by adding the new element
            current_sum += nums[right]
            
            # 2. Shrink the window from the left while the sum is healthy (>= target)
            while current_sum >= target:
                # Update our record shortest length
                min_len = min(min_len, right - left + 1)
                
                # Subtract the leaving element and slide left forward
                current_sum -= nums[left]
                left += 1
                
        # If min_len was updated, return it. Otherwise, return 0.
        return min_len if min_len != float('inf') else 0