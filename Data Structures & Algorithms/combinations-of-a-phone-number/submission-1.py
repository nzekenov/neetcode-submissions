class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        results = []

        def backtrack(i, path):
            if i == len(digits):
                results.append(path)
                return

            for letter in letters[int(digits[i])]:
                backtrack(i+1, path+letter)

        if len(digits) > 0:
            backtrack(0, "")
        return results