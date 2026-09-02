class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        total = numbers[l] + numbers[r]
        while total != target:
            if total > target:
                r -= 1
            else:
                l += 1
            # update total
            total = numbers[l] + numbers[r] 
        return [l + 1, r + 1]