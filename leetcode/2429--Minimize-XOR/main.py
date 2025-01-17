from typing import List

def dec2bin(n: int) -> List[int]:
    if n == 0: return [0]

    sum_d = 0
    bin_stack = []
    while n > 0:
        i = n%2
        bin_stack.append(i)
        n = n//2
        sum_d += i
    return bin_stack[::-1]


def bin2dec(bin_num: List[int]) -> int:
    dec = 0
    for i in range(len(bin_num)):
        dec += bin_num[-1-i] * (2 ** i)
    
    return dec


class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bin1 = dec2bin(num1)
        sum_bin1 = sum(bin1)
        bin2 = dec2bin(num2)
        sum_bin2 = sum(bin2)

        min_xor_with_2 = list()
        if sum_bin1 >= sum_bin2:
            # print('sum_bin1 >= sum_bin2')
            i = 0
            while sum_bin2 > 0:
                if bin1[i] == 1:
                    # min_xor_with_2.append(1)
                    sum_bin2 -= 1
                # else: min_xor_with_2.append(0)
                min_xor_with_2.append(bin1[i])
                i += 1
            while i < len(bin1):
                min_xor_with_2.append(0)
                i += 1
        else:
            if sum_bin2 < len(bin1):
                # print('sum_bin2 < len(bin1)')
                sum_bin2 = sum_bin2 - sum_bin1
                i = len(bin1) -1 
                while sum_bin2 > 0:
                    if bin1[i] == 0:
                        sum_bin2 -= 1
                        bin1[i] = 1
                    i -= 1
                min_xor_with_2 = bin1
            else:
                # print('not sum_bin2 < len(bin1)')
                min_xor_with_2 = [1] * len(bin1)
                sum_bin1 = len(bin1)
                while sum_bin1 < sum_bin2:
                    min_xor_with_2.insert(0, 1)
                    sum_bin1 += 1

        return bin2dec(min_xor_with_2)




if __name__ == '__main__':
    for num in [8, 75, 15]:
        # num = 0
        print('*'*20)
        print('input decimal is {}'.format(num))
        bin_num = dec2bin(num)
        print(''.join([str(d) for d in bin_num ]))
        print(bin2dec(bin_num))
