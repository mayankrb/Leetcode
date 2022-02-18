class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited_dict = {}
        max_len = 0
        lagging, forward = 0, 0
        for forward in range(len(s)):
            if (s[forward] not in visited_dict.keys()) or (visited_dict[s[forward]]==0):
                visited_dict[s[forward]] = 1
                if forward-lagging+1>max_len:
                    max_len = forward-lagging+1
                    #print(forward, lagging, max_len)
            else:
                while s[lagging]!=s[forward]:
                    visited_dict[s[lagging]]-=1
                    lagging+=1
                lagging+=1
                #print(forward, lagging, max_len)
        return max_len