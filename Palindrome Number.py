class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        temp = x
        reverse_num = 0
        while temp:
            reverse_num = reverse_num*10+ temp%10
            temp = temp//10
        if reverse_num == x:
            return True
        return False
            