# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if sorted(s) == sorted(t):
#             return True
#         else:
#             return False











class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if sorted(t) == sorted(s):
            return True
        else:
            return False