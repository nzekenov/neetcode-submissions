class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, current_path, current_sum):
            if current_sum == target:
                res.append(current_path.copy())
                return

            if i >= len(nums) or current_sum > target:
                return
            
            current_path.append(nums[i])
            dfs(i, current_path, current_sum + nums[i])
            
            current_path.pop()
            dfs(i + 1, current_path, current_sum)

        dfs(0, [], 0)
        return res