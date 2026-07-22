class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        candidates.sort()
        def backtrack(i, current_sum, path):
            if current_sum == target:
                results.append(path[:])
                return

            if i == len(candidates) or current_sum > target:
                return
        
            path.append(candidates[i])
            backtrack(i+1, current_sum + candidates[i], path)
            path.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i+1, current_sum, path)
                
        backtrack(0, 0, [])
        return results