class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        current_palindrome = []

        def backtrack(i):
            if i >= len(s):
                res.append(current_palindrome.copy())
                return
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]: 
                    current_palindrome.append(s[i : j + 1])
                    backtrack(j + 1)
                    current_palindrome.pop()

        backtrack(0)
        return res
                