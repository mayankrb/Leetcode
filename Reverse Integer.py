class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        max_val = 2<<31 -1
        min_val = -(max_val+1)
        if x < 0:
            sign = -1
            x = -x
        result = 0
        while x > 0:
            result = result*10 + x%10
            x = x//10
        result *= sign
        if result < min_val or result > max_val:
            result = 0
        return result