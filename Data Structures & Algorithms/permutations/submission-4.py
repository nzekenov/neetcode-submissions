class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        visited = set()
        def backtrack(path):
            if len(path) == len(nums):
                results.append(path.copy())
                return

            for num in nums:
                if num not in visited:
                    path.append(num)
                    visited.add(num)
                    backtrack(path)
                    path.pop()
                    visited.remove(num)
        backtrack([])
        return results