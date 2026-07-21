class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-/*":
                item1 = stack.pop()
                item2 = stack.pop()
                if token == "+":
                    res = item2 + item1
                elif token == "-":
                    res = item2 - item1
                elif token == "*":
                    res = item2 * item1
                else:
                    res = int(float(item2) / item1)
                stack.append(res)
            else:
                stack.append(int(token))
        return stack.pop()