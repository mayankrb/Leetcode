class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        val_dict = {ch: ord(ch)-ord('A')+1 for ch in "QWERTYUIOPLKJHGFDSAZXCVBNM"}
        col_num = 0
        for i in range(len(columnTitle)):
            order = len(columnTitle)-1-i
            ch = columnTitle[i]
            col_num += val_dict[ch] * int(pow(26, order))
        return col_num