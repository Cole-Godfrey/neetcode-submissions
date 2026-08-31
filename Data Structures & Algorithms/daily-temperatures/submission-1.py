class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # [temp, idx]
        
        for i in range(len(temperatures)):
            if not stack:
                stack.append([temperatures[i], i])
                continue
            while stack and temperatures[i] > stack[-1][0]:
                result[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append([temperatures[i], i])
        
        return result

