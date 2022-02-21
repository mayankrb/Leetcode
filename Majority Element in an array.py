class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cur_cand, cur_count = nums[0], 1
        majority_element_count = 0
        for i in range(1, len(nums)):
            if cur_cand == nums[i]:
                cur_count+=1
            else:
                if cur_count == 1:
                    cur_cand = nums[i]
                else:
                    cur_count-=1
                    
        #can directly return cur_candidate cause we are guaranteed to have one
        return cur_cand
        '''
        #if no guarantee of majority element
        for num in nums:
            if num == cur_cand:
                majority_element_count+=1
        
        if majority_element_count >= len(nums)//2:
            return cur_cand
        else:
            return -1
        '''