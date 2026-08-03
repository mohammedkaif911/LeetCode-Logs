class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanChar = []
        for a in s:
            if a.isalnum():
                cleanChar.append(a.lower())
            

        return cleanChar == cleanChar[::-1]