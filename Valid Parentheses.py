class Solution:
    def isValid(self, s: str) -> bool:
        myqueue = []
        for char in s:
            if char in ['(','[','{']:
                myqueue.append(char)
            else:
                if not myqueue:
                    return False
                if char=='}' and myqueue[-1] == '{':
                    myqueue.pop()
                elif char==')' and myqueue[-1] == '(':
                    myqueue.pop()
                elif char==']' and myqueue[-1] == '[':
                    myqueue.pop()
                else:
                    return False
        if myqueue:
            return False
        return True