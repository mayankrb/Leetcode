import heapq

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        max_num, min_num = -1, 1000000001
        min_diff = 1000000001
        #make every number its max value possible, then we will reduce them
        for i in range(len(nums)):
            if nums[i]%2==1:
                nums[i] *= 2        
        my_heap = []
        for num in nums:
            heapq.heappush(my_heap, (-num, num))
            max_num = max(max_num, num)
            min_num = min(min_num, num)
            
        while my_heap:
            _, cur_top = heapq.heappop(my_heap)  
            if cur_top%2==1:
                break
            min_diff = min(cur_top-min_num, min_diff)      
            cur_top//=2
            min_num = min(cur_top, min_num)
            heapq.heappush(my_heap, (-cur_top, cur_top))
        
        min_diff = min(min_diff, cur_top - min_num)
        #print(min_num, max_num)
            
        return min_diff