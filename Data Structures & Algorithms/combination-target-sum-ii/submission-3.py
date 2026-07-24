class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        results = []

        def backtrack(i, path, remainder):
            if remainder == 0:
                results.append(path.copy())
                return
            
            if i == len(candidates) or remainder - candidates[i] < 0:
                return
            
            path.append(candidates[i])
            backtrack(i+1,path,remainder-candidates[i])
            path.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            print(f"We got {i+1}")
            backtrack(i+1,path,remainder)

        
        backtrack(0, [], target)
        return results