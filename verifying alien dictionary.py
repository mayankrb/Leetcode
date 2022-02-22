class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        def is_second_one_smaller(st1, st2, order_dict):
            #len_flag = False means length of first string is smaller 
            #-1 means first one is smaller, 1 means second one is smaller, 0 means equal. Lexicographically
            
            second_len_larger_flag = False
            
            small_len = min(len(st1), len(st2))
            
            if len(st1) <= len(st2):
                second_len_larger_flag = True
            
            for i in range(small_len):
                if order_dict[st1[i]] < order_dict[st2[i]]:
                    return False
                if order_dict[st1[i]] > order_dict[st2[i]]:
                    return True
            
            if second_len_larger_flag:
                return False
            return True
        
        
        
        #if only one word, it is True always
        if len(words)==1:
            return True
        
        order_dict = {}
        for i in range(26):
            order_dict[order[i]] = i
        
        for i in range(len(words)-1):
            if is_second_one_smaller(words[i], words[i+1], order_dict):
                return False
        return True
                