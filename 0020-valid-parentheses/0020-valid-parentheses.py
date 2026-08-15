class Solution:
    def isValid(self, s: str) -> bool:
        obrackets = {"(":")","[":"]","{":"}"}
        cbrackets = {")":"(","]":"[","}":"{"}
        braces = []
        if s[0] in cbrackets:
            return False
        elif s[-1] in obrackets:
            return False
        else:
            for b in s:
                if b in obrackets:
                    braces.append(b)
                elif braces and cbrackets[b] == braces[-1]:
                    braces.pop()
                else:
                    return False
                
        if len(braces) == 0:
            return True
        else:
            return False
                    



        