from collections import deque
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        cur_removed_count = 0
        stack = deque()
        for i in range(len(num)):
            while cur_removed_count<k and stack and stack[-1] > int(num[i]):
                stack.pop()
                cur_removed_count+=1
                
            stack.append(int(num[i]))
        #print(stack)
        while cur_removed_count < k and stack: 
            top = stack[-1]
            stack.pop()
            if stack and stack[-1]>top:
                stack.pop()
                stack.append(top)
            cur_removed_count+=1
        
        if not stack:
            return "0"
        
        
        all_zero_flag = True
        ans_list = []
        while stack:
            num = stack[-1]
            if num!=0:
                all_zero_flag= False
            ans_list.append(str(num))
            stack.pop()
            
        #print(ans_list)
        if all_zero_flag:
            return "0"
        ans_list.reverse()
        for i in range(len(ans_list)):
            if ans_list[i]!='0':
                return ''.join(ans_list[i:])