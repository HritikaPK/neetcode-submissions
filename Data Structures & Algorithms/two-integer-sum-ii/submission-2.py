class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
    
        for i in range(0,len(numbers)):
            j = len(numbers) - 1
            while j>i:
                if numbers[i] == numbers[j]:
                    j -= 1
                elif numbers[i] + numbers[j] == target:
                    return [i+1,j+1]
                else: 
                    j -= 1
        