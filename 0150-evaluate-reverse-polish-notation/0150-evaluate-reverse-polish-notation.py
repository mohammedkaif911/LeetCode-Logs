class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for n in tokens:
            if n == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                result = int(num2 / num1)
                stack.append(result)
            elif n == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                result = num1 + num2
                stack.append(result)
            elif n == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                result = num2 - num1
                stack.append(result)
            elif n == "*":
                num1 = stack.pop()
                num2 = stack.pop()
                result = num1 * num2
                stack.append(result)
            else:
                stack.append(int(n))
        res = stack[-1]
        return res
                