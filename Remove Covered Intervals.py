class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        #sort based on start_time(increasing), end_time(decreasing)
        intervals.sort(key = lambda x: (x[0], -x[1]))
        prev_interval, cur_interval = intervals[0], []
        count = 1
        #print(intervals)
        for i in range(1, len(intervals)):
            cur_interval = intervals[i]
            if cur_interval[1] > prev_interval[1]:
                prev_interval = cur_interval[:]
                count+=1
        return count