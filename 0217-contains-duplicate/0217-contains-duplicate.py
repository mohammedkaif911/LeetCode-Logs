# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         set_nums = len(list(set(nums)))
#         if set_nums == len(nums):
#             return False
#         else:
#             return True
        

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        if len(set(nums)) == len(nums):
            return False
        else:
            return True

