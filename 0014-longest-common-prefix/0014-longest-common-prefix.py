class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        pre = ""
        last = (len(strs)-1)
        for i in range(0,len(strs[0])):
            if strs[0][i] == strs[last][i]:
                pre = pre + strs[0][i]
            else:
                return pre
        return pre
        
        
        