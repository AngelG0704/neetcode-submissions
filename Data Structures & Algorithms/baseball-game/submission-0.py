class Solution:
    def calPoints(self, operations: List[str]) -> int:
        total = 0
        stack = []

        for ch in operations:
            if ch == "+":
                stack.append(stack[-2]+stack[-1])
                total += stack[-1]
            elif ch == "D":
                stack.append(stack[-1]*2)
                total += stack[-1]
            elif ch == "C":
                total -= stack[-1]
                stack.pop()
            else:
                x = int(ch)
                stack.append(x)
                total += stack[-1]
        return total