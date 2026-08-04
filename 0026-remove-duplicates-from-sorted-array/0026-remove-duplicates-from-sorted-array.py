class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write_ptr = 1
        for left_ptr in range(1,len(nums)):
            if nums[left_ptr] != nums[left_ptr-1]:
                nums[write_ptr]=nums[left_ptr]
                write_ptr+=1

        return write_ptr
                
        