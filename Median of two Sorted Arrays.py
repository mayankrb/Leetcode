class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        #if one of the array is empty, return the median from the other array
        if len(nums2)==0:
            nums1, nums2 = nums2, nums1
        if len(nums1)==0:
            length, ind = len(nums2), (len(nums2)-1)//2
            median = nums2[ind]
            if length%2==0:
                median+=nums2[ind+1]
                median/=2.0
            return median
        
        
        smaller_arr, larger_arr = nums1, nums2
        if len(smaller_arr)>len(larger_arr):
            smaller_arr, larger_arr = larger_arr, smaller_arr
        
        
        #median index of merged arrays
        total_len = (len(smaller_arr)+len(larger_arr))
        median_ind = (total_len-1)//2
        
        #edge cases
        #case 1: arrays have equal size and median is the average of last element of one array and first element of the other array, 
        #case 2: no element is used from smaller array for calculation,ex: smaller_arr=[4] larger_arr = [1,2,3,5], deal with this case
        #case 3: otherwise
        
        #case: equal length and one array's last element and second one's first one is used
        if len(smaller_arr)==len(larger_arr):
            if smaller_arr[-1] <= larger_arr[0]:
                return (smaller_arr[-1]+larger_arr[0])/2.0
            if smaller_arr[0] >= larger_arr[-1]:
                return (smaller_arr[0]+larger_arr[-1])/2.0
        #case: no element from smaller_arr is a participant in calc, ex: smaller_arr=[4] larger_arr = [1,2,3,5], we need to go before 0 index, which is not possible,
        if len(smaller_arr) < len(larger_arr):
            #if no element is used from the smaller array
            if smaller_arr[-1] <= larger_arr[0]:
                ind = median_ind - len(smaller_arr)
                median = larger_arr[ind]
                if total_len%2==0:
                    median+=larger_arr[ind+1]
                    median/=2.0
                return median
            if smaller_arr[0] >= larger_arr[median_ind]:
                median = larger_arr[median_ind]
                if total_len%2==0:
                    median+=min(larger_arr[median_ind+1], smaller_arr[0])
                    median/=2.0
                return median
            #find_upper_bound
            
        
        
        smaller_arr.append(1000000001)
        larger_arr.append(1000000001)
        
        
        
        st, end = 0, len(smaller_arr)-2
        mid1 = (st+end)//2
        mid2 = median_ind-mid1-1
        while st <= end:
            #print(st, end)
            mid1 = (st+end)//2
            mid2 = median_ind-mid1-1
            #print(mid1, mid2)
            if smaller_arr[mid1] <=  larger_arr[mid2+1] and larger_arr[mid2] <= smaller_arr[mid1+1]:
                #print("In this condition ", mid1, " ", mid2)
                median = max(smaller_arr[mid1], larger_arr[mid2])
                if total_len%2==0:
                    median+=min(smaller_arr[mid1+1], larger_arr[mid2+1])
                    median/=2.0
                return median
            if smaller_arr[mid1] >= larger_arr[mid2+1]:
                end = mid1-1
            else:
                st = mid1+1
            
        mid1, mid2 = st, median_ind-st-1
        #print(mid1, mid2)
        median = max(smaller_arr[mid1], larger_arr[mid2])
        if total_len%2==0:
            median+=min(smaller_arr[mid1+1], larger_arr[mid2+1])
            median/=2.0
        return median