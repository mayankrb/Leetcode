from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #falg to check if every element is 0 or not
        flag_zero = True
        m, n = len(grid), len(grid[0])
        visited = [[False for j in range(n)] for i in range(m)]
        minute_to_get_rotten = [[10000000 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]!=0:
                    flag_zero = False
                if grid[i][j]==2:
                    minute_to_get_rotten[i][j] = 0
        
        #if there are no oranges return 0
        if flag_zero:
            return 0
        
        #for every rotten orange, use it as a starting node and apply bfs to find the minimum times possible
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    #apply bfs and update the cells that we can minimize
                    bfs_queue = deque()
                    visited = [[False for j in range(n)] for i in range(m)]
                    bfs_queue.append([[i, j], 0])
                    while bfs_queue:
                        indices, cur_minutes = bfs_queue[0]
                        cur_row, cur_col = indices
                        bfs_queue.popleft()
                        if cur_row-1>=0 and grid[cur_row-1][cur_col]!=0 and minute_to_get_rotten[cur_row-1][cur_col]>cur_minutes+1:
                            minute_to_get_rotten[cur_row-1][cur_col]=cur_minutes+1
                            bfs_queue.append([[cur_row-1, cur_col], cur_minutes+1])
                        if cur_row+1<m and grid[cur_row+1][cur_col]!=0 and minute_to_get_rotten[cur_row+1][cur_col]>cur_minutes+1:
                            minute_to_get_rotten[cur_row+1][cur_col]=cur_minutes+1
                            bfs_queue.append([[cur_row+1, cur_col], cur_minutes+1])
                        if cur_col-1>=0 and grid[cur_row][cur_col-1]!=0 and minute_to_get_rotten[cur_row][cur_col-1]>cur_minutes+1:
                            minute_to_get_rotten[cur_row][cur_col-1]=cur_minutes+1
                            bfs_queue.append([[cur_row, cur_col-1], cur_minutes+1])
                        if cur_col+1<n and grid[cur_row][cur_col+1]!=0 and minute_to_get_rotten[cur_row][cur_col+1]>cur_minutes+1:
                            minute_to_get_rotten[cur_row][cur_col+1]=cur_minutes+1
                            bfs_queue.append([[cur_row, cur_col+1], cur_minutes+1])
        
        #get the maximum time taken by any orange if a orange is still fresh then we return -1
        max_time = -1
        for i in range(m):
            for j in range(n):
                if grid[i][j]!=0:
                    if minute_to_get_rotten[i][j]==10000000:
                        return -1
                    max_time = max(max_time, minute_to_get_rotten[i][j])
        
        return max_time