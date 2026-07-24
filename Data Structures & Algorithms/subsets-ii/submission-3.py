class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        def backtrack(path, i):
            if i == len(nums):
                results.append(path.copy())
                return 

            path.append(nums[i])
            backtrack(path, i+1)
            path.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            backtrack(path, i+1)
            

        backtrack([], 0)
        return results