from typing import List

def dec2bin(n: int) -> List[int]:
    """
    Convert decimal number to binary representation as a list of integers.
    
    Args:
        n (int): Decimal number to convert
        
    Returns:
        List[int]: Binary representation as list of 0s and 1s, most significant bit first
        
    Example:
        >>> dec2bin(5)
        [1, 0, 1]
    """
    if n == 0:
        return [0]
    
    bin_stack = []
    while n:
        bin_stack.append(n & 1)  # Using bitwise AND for modulo 2
        n >>= 1  # Using right shift for division by 2
    
    return bin_stack[::-1]

def bin2dec(bin_num: List[int]) -> int:
    """
    Convert binary representation (as list of integers) to decimal number.
    
    Args:
        bin_num (List[int]): Binary representation as list of 0s and 1s
        
    Returns:
        int: Decimal representation
        
    Example:
        >>> bin2dec([1, 0, 1])
        5
    """
    return sum(digit * (1 << i) for i, digit in enumerate(reversed(bin_num)))

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        """
        Find a number that has the same number of set bits (1s) as num2 and 
        minimizes the XOR value when XORed with num1.
        
        Args:
            num1 (int): First number
            num2 (int): Second number, used to determine number of set bits
            
        Returns:
            int: Number that minimizes XOR with num1 while having same number of set bits as num2
            
        Example:
            >>> s = Solution()
            >>> s.minimizeXor(3, 5)  # 3 (11) XOR 5 (101)
            3
        """
        bin1 = dec2bin(num1)
        target_ones = bin(num2).count('1')  # More efficient way to count set bits
        
        # Case 1: When target_ones is greater than or equal to bits in num1
        if target_ones >= len(bin1):
            result = ['1'] * len(bin1)
            # Add remaining 1s to the left
            result = ['1'] * (target_ones - len(bin1)) + result
            return int(''.join(result), 2)
        
        # Case 2: When target_ones is less than bits in num1
        result = ['0'] * len(bin1)
        
        # First, copy 1s from most significant positions in num1
        ones_needed = target_ones
        for i in range(len(bin1)):
            if bin1[i] == 1 and ones_needed > 0:
                result[i] = '1'
                ones_needed -= 1
                
        # If we still need more 1s, put them in least significant 0 positions
        i = len(bin1) - 1
        while ones_needed > 0 and i >= 0:
            if result[i] == '0':
                result[i] = '1'
                ones_needed -= 1
            i -= 1
        
        return int(''.join(result), 2)
