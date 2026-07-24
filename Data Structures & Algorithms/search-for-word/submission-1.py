class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(row, col, i):
            if i == len(word):
                return True

            if not (0 <= row < rows) or not (0 <= col < cols):
                return False
                
            if board[row][col] != word[i]:
                return False

            board[row][col] = "?"
            found = False   
            for r, c in ((-1,0), (0,1), (0,-1), (1,0)):
                found |= dfs(row+r, col+c, i+1)
            board[row][col] = word[i]
            return found

        return any(dfs(i,j,0) for i in range(rows) for j in range(cols))
        