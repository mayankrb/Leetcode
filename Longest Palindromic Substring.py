class Solution:
    dp = [[0 for i in range(1001)]for i in range(1001)]
    visited = [[0 for i in range(1001)]for i in range(1001)]
    start_end = [[[0, 0] for i in range(1001)]for i in range(1001)]
    for i in range(1001):
        dp[i][i] = 1
        start_end[i][i] = [i, i]
    def solve(self, string, start, end):
        if start == end:
            return 1, start, end
        if self.visited[start][end] == 1:
            return self.visited[start][end], self.start_end[start][end][0], self.start_end[start][end][1]
        option1_len, start1, end1 = self.solve(string, start+1, end)
        option2_len, start2, end2 = self.solve(string, start, end-1)
        final_option, final_start, final_end = 0, 0, 0
        if option2_len < option1_len:
            final_option, final_start, final_end = option1_len, start1, end1
        else:
            final_option, final_start, final_end = option2_len, start2, end2
        if string[start] == string[end] and self.dp[start+1][end-1]==(end-start-1):
            final_option, final_start, final_end = end-start+1, start, end
        
        self.dp[start][end] = final_option
        self.visited[start][end]= 1
        self.start_end[start][end] = [final_start, final_end]
        return self.dp[start][end], final_start, final_end
    
    def solve_2_centre(self, s, centre):
        centre1, centre2 = centre, centre+1
        left, right = -1, len(s)
        palin_len = 0
        palin_start = centre
        while centre1 > left and centre2 < right:
            if s[centre1] == s[centre2]:
                palin_len += 2
                palin_start = centre1
                centre1-=1
                centre2+=1
            else:
                break
        return palin_start, palin_len
    
    def solve_1_centre(self, s, centre):
        centre1, centre2 = centre-1, centre+1
        left, right = -1, len(s)
        palin_len = 1
        palin_start = centre
        while centre1 > left and centre2 < right:
            if s[centre1] == s[centre2]:
                palin_len += 2
                palin_start = centre1
                centre1-=1
                centre2+=1
            else:
                break
        return palin_start, palin_len
    
    def solve_with_centres(self, s):
        if len(s)==1:
            return s
        max_len = 0
        max_start_ind = -1
        for centre in range(len(s)):
            cur_start_ind, cur_len = self.solve_1_centre(s, centre)
            #print(centre, cur_len, cur_start_ind, False)
            if max_len<cur_len:
                max_len, max_start_ind = cur_len, cur_start_ind
            if centre<len(s)-1 and s[centre] == s[centre+1]:
                cur_start_ind, cur_len = self.solve_2_centre(s, centre)
                #print(centre, cur_len, cur_start_ind, True)
                if max_len<cur_len:
                    max_len, max_start_ind = cur_len, cur_start_ind
        return s[max_start_ind : max_start_ind+max_len]
        
    def longestPalindrome(self, s: str) -> str:
        #_, start, end = self.solve(s, 0, len(s)-1)
        #return s[start:end+1]
        longestPalin = self.solve_with_centres(s)
        return longestPalin