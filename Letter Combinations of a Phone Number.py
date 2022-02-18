class Solution:
    
    def solve_letter_combinations(self, digits, cur_ind, cur_str, ans, letter_dict):
        if cur_ind >= len(digits):
            ans.append(''.join(cur_str))
            return ans
        digit = int(digits[cur_ind])
        words = letter_dict[digit]
        for word in words:
            cur_str[cur_ind] = word
            self.solve_letter_combinations(digits, cur_ind+1, cur_str, ans, letter_dict)
        return ans
    
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        cur_str = ['' for i in range(len(digits))]
        ans = []
        letter_dict = {
            2: 'abc', 3: 'def', 4: 'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'
        }
        ans = self.solve_letter_combinations(digits, 0, cur_str, ans, letter_dict)
        return ans