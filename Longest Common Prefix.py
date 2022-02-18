class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = len(strs[0])
        for s in strs:
            min_len = min(len(s), min_len)
        
        ans = []
        for i in range(min_len):
            char = strs[0][i]
            flag = 0
            for s in strs:
                if char!=s[i]:
                    flag = 1
                    break
            if flag:
                break
            ans.append(char)
        
        return "".join(ans)
                