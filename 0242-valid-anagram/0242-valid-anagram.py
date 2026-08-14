# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if sorted(s) == sorted(t):
#             return True
#         else:
#             return False











class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        T = sorted(t)
        S = sorted(s)
        if S == T:
            return True
        else:
            return False