from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        current_subset = []
        def dfs(i) -> None:
            if i >= len(nums):
                res.append(current_subset.copy())
                return
            
            current_subset.append(nums[i])
            dfs(i + 1)

            current_subset.pop()
            dfs(i + 1)
        dfs(0)

        return res