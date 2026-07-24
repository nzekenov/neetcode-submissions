class Solution:
    def partition(self, s: str) -> List[List[str]]:
        results = []

        def backtrack(i, path):
            if i == len(s):
                results.append(path.copy())
                return
            
            for j in range(i+1, len(s) + 1):
                piece = s[i:j]
                if piece == piece[::-1]:
                    path.append(piece)
                    backtrack(j, path)
                    path.pop()
        
        backtrack(0, [])
        return results