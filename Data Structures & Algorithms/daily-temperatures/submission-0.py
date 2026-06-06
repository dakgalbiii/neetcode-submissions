class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tempStack = []
        output = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while tempStack and temperatures[i] > temperatures[tempStack[-1]]:
                idx = tempStack.pop()
                output[idx] = i - idx
            tempStack.append(i)
        
        return output