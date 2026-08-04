class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        k = len(needle)
        l = len(haystack)
        for i in range(0,l-k+1):
            if needle == haystack[i:i+k]:
                return i
            
        return -1
        