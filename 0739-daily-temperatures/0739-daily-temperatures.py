class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        answer = [0] * n
        stack = []              # holds INDICES of unresolved days

        for i in range(n):
            # While today is hotter than the day on top of the stack...
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()          # that day finally gets its answer
                answer[prev] =i - prev         # distance = today - that day
            stack.append(i)              # today becomes an unresolved day
        return answer
        