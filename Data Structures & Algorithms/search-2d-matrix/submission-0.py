class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r_lo, r_hi = 0,  len(matrix) - 1
        while r_lo <= r_hi:
            r_mid = r_lo + (r_hi - r_lo) // 2
            if matrix[r_mid][0] > target:
                r_hi = r_mid - 1
            elif matrix[r_mid][-1] < target:
                r_lo = r_mid + 1
            else:
                break;

        if not r_lo <= r_hi:
            return False
        
        r_mid = r_lo + (r_hi - r_lo) // 2
        l, r = 0, len(matrix[r_mid]) - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[r_mid][m]:
                l = m + 1
            elif target < matrix[r_mid][m]:
                r = m - 1
            else:
                return True
        return False


        # ## First option
        # ROWS, COLS = len(matrix), len(matrix[0])

        # top, bot = 0, ROWS - 1
        # while top <= bot:
        #     row = (top + bot) // 2
        #     if target > matrix[row][-1]:
        #         top = row + 1
        #     elif target < matrix[row][0]:
        #         bot = row - 1
        #     else:
        #         break

        # if not (top <= bot):
        #     return False
        # row = (top + bot) // 2
        # l, r = 0, COLS - 1
        # while l <= r:
        #     m = (l + r) // 2
        #     if target > matrix[row][m]:
        #         l = m + 1
        #     elif target < matrix[row][m]:
        #         r = m - 1
        #     else:
        #         return True
        # return False

        ## Second option
        # ROWS, COLS = len(matrix), len(matrix[0])

        # l, r = 0, ROWS * COLS - 1
        # while l <= r:
        #     m = l + (r - l) // 2
        #     row, col = m // COLS, m % COLS
        #     if target > matrix[row][col]:
        #         l = m + 1
        #     elif target < matrix[row][col]:
        #         r = m - 1
        #     else:
        #         return True
        # return False