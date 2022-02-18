class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i in range(len(nums)):
            key = target-nums[i]
            if key in my_dict.keys():
                ans = [my_dict[key], i]
                break
            else:
                my_dict[nums[i]] = i
        return ans