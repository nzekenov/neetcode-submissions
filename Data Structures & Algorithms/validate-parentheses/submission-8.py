class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in "{[(":
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                item = stack.pop()
                if char == "}" and item != "{":
                    return False
                elif char == "]" and item != "[":
                    return False
                elif char == ")" and item != "(":
                    return False
                else:
                    continue
        
        return len(stack) == 0