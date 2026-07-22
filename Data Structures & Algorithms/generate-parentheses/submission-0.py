class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []

        def backtrack(l, r, current):
            if l == n and r == n:
                results.append(current)
                return

            if l > n:
                return
            
            if r > l:
                return

            current += "("
            backtrack(l+1, r, current)
            current = current[:-1]
            current += ")"
            backtrack(l, r+1, current)            
            
        backtrack(0, 0, "")
        return results