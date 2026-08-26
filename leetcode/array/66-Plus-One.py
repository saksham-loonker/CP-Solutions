class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        big_number = 0
        real_digits = digits[::-1]
        for i in range(0,len(real_digits)):
            big_number += real_digits[i]*(10**i)
        big_number += 1
        final = list(map(int, str(big_number)))
        return final