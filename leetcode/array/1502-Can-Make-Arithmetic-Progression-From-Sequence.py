class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr1 = sorted(arr)
        diff = arr1[1] - arr1[0]
        for i in range(2, len(arr1)):
            if (arr1[i] - arr1[i-1]) != diff:
                return False  
        return True 
