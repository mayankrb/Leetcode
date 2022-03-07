class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count_dict = {}
        empty_count = 0
        for s in strs:
            if len(s)==0:
                empty_count+=1
                continue
            chars = [ch for ch in s]
            chars.sort()
            sorted_s = ''.join(chars)
            try:
                count_dict[sorted_s].append(s)
            except:
                count_dict[sorted_s] = [s]
        ans = []
        if empty_count > 0:
            ans.append(["" for i in range(empty_count)])
        for key in count_dict.keys():
            ans.append(count_dict[key])
        return ans