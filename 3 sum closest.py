class Solution:
    
    def lower_bound(self, arr, start, end, target):
        if target < arr[start]:
            return start-1
        if target > arr[end]:
            return end+1
        while start<end:    
            mid = (start+end)//2
            if arr[mid] < target:
                start = mid+1
            else:
                end = mid
        return start
    
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        max_diff = 100000000000000
        closest_sum = -1
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                key = target-(nums[i]+nums[j])
                ind = self.lower_bound(nums, j+1, len(nums)-1, key)
                
                if ind >= len(nums):
                    sum_ = nums[i] + nums[j] + nums[-1]
                    diff = abs(sum_ - target)
                    if diff < max_diff:
                        max_diff = diff
                        closest_sum = sum_
                elif ind <= j:
                    sum_ = nums[i] + nums[j] + nums[j+1]
                    diff = abs(sum_ - target)
                    if diff < max_diff:
                        max_diff = diff
                        closest_sum = sum_
                else:
                    sum_ = nums[i] + nums[j] + nums[ind]
                    diff = abs(sum_ - target)
                    if diff < max_diff:
                        max_diff = diff
                        closest_sum = sum_
                        
                    sum_ = nums[i] + nums[j] + nums[ind-1]
                    diff = abs(sum_ - target)
                    if diff < max_diff:
                        max_diff = diff
                        closest_sum = sum_
                    if ind < len(nums)-1:
                        sum_ = nums[i] + nums[j] + nums[ind+1]
                        diff = abs(sum_ - target)
                        if diff < max_diff:
                            max_diff = diff
                            closest_sum = sum_
        return closest_sum