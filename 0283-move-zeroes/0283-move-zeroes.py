class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        current_index = 0
        for num in range(len(nums)):
            if nums[num] != 0:
                nums[num] , nums[current_index] = nums[current_index] , nums[num]
                current_index+=1
            
        """
        Do not return anything, modify nums in-place instead.
        """
        