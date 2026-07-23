class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        nums.sort()
        def backtrack(i, current_sum, path):
            if current_sum == target:
                results.append(path.copy())
                return

            for j in range(i, len(nums)):
                if current_sum + nums[j] > target:
                    return
                path.append(nums[j])
                backtrack(j, current_sum + nums[j], path)
                path.pop()

        backtrack(0, 0, [])
        return results