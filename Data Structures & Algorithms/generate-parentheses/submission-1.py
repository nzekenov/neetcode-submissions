class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []

        def backtrack(nL, nR, path):
            if nR == n:
                results.append(path)
                return

            if nL < n:
                backtrack(nL+1, nR, path+"(")

            if nR < nL:
                backtrack(nL, nR+1, path+")")

        backtrack(0, 0, "")
        return results