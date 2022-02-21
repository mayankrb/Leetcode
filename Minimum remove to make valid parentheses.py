from collections import deque
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        valid = [True for i in range(len(s))]
        ans_str = []
        my_stack = deque()
        for i in range(len(s)):
            ch = s[i]
            if ch==')':
                if not my_stack:
                    valid[i]=False
                else:
                    my_stack.pop()
            if ch=='(':
                my_stack.append(i)
        while my_stack:
            valid[my_stack[-1]] = False
            my_stack.pop()
        
        for i in range(len(s)):
            if valid[i]:
                ans_str.append(s[i])
        return "".join(ans_str)
        