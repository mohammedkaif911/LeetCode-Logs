class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = ""
        max_len = 0
        
        for char in s:
            # 1. If char is already in seen, cut off everything up to that duplicate
            if char in seen:
                seen = seen[seen.index(char) + 1:]
            
            # 2. Add current char
            seen += char
            
            # 3. Keep track of the longest string length
            if len(seen) > max_len:
                max_len = len(seen)
                
        return max_len
        