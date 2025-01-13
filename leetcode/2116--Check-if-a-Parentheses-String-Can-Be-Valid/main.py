from collections import defaultdict

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n_s = len(s)
        if n_s % 2 == 1: return False

        open_bracket_num = 0
        unlock_bracket_num = 0

        for i in range(n_s):
            if locked[i] == '0':
                unlock_bracket_num += 1
            elif s[i] == '(': # locked open parenthesis
                open_bracket_num += 1
            else: # locked close parenthesis
                if open_bracket_num > 0: open_bracket_num -= 1
                elif unlock_bracket_num > 0: unlock_bracket_num -= 1
                else: return False

        balance = 0
        for i in range(n_s - 1, -1, -1):
            if locked[i] == 0:
                balance -= 1
                unlock_bracket_num -= 1
            elif s[i] == '(':
                balance += 1
                open_bracket_num -= 1
            if balance > 0: return False
            if unlock_bracket_num * open_bracket_num == 0:break
        if open_bracket_num > 0 or unlock_bracket_num % 2 != 0: return False

        return True
       

    def canBeValid_v1(self, s: str, locked: str) -> bool:
        n_s = len(s)
        if n_s % 2 == 1: return False
        
        # '(': -1, ')': 1, 'unlocked': 0
        open_par_stack = list()
        par_dict = defaultdict( lambda: 0)
        par_dict.update({'(':-1, ')':1})

        indices = []
        for i, (l, c) in enumerate(zip(locked, s)):
            # print(''.join( ['*']*i+[str(i)]+['*']*(len(s) - i - 1)), open_par_stack, indices)
            if not len(open_par_stack):
                if l == '1':
                    open_par_stack.append(par_dict[c])
                else: 
                    open_par_stack.append(par_dict['unlocked'])
                indices.append(i)
                continue
            
            if l == '1':
                last_par_value = open_par_stack[-1]
                par_sum = abs(last_par_value + par_dict[c])
                if par_sum < 2:
                    if par_sum == 1 or (par_sum == 0 and last_par_value == -1 and par_dict[c] == 1) or (par_sum == 0 and last_par_value == 0 and par_dict[0] == 0):
                        open_par_stack.pop()
                        indices.pop()
                        continue
            open_par_stack.append(par_dict[c] if l == '1' else par_dict['unlocked'])
            indices.append(i)
        print(open_par_stack, indices)
        return len(open_par_stack) >= abs(sum(open_par_stack))
