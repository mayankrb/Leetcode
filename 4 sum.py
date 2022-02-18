class Solution:
    
    def index_matches(self, indexes, c):
        for index in indexes:
            if index > c:
                return False
        return True
    
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        my_dict = {}
        my_set = set()
        ans = []
        for i in range(len(nums)):
            try:
                my_dict[nums[i]].append(i)
            except:
                my_dict[nums[i]] = [i]
        
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                for k in range(j+1, len(nums)-1):
                    key = target-(nums[i]+nums[j]+nums[k])
                    if key in my_dict.keys():
                        indexes = my_dict[key]
                        if self.index_matches(indexes, k)==False:
                            vals = sorted([str(nums[i]), str(nums[j]), str(nums[k]), str(key)])
                            s = '.'.join(vals)
                            if s not in my_set:
                                my_set.add(s)
                                ans.append(vals)
                            
        return ans