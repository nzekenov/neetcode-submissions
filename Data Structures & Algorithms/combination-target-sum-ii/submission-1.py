class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        current_path = []
        def dfs(i, current_sum):
            if current_sum == target:
                res.append(current_path.copy())
                return
            if current_sum > target or i >= len(candidates):
                return
            
            current_path.append(candidates[i])
            dfs(i + 1, current_sum + candidates[i])

            current_path.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1, current_sum)

        dfs(0, 0)
        return res
