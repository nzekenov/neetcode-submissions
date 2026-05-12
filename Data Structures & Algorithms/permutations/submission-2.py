from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(idx):
            if idx == len(nums):
                res.append(nums.copy())
                return
            for i in range(idx, len(nums)):
                nums[idx], nums[i] = nums[i], nums[idx]
                backtrack(idx + 1)
                nums[idx], nums[i] = nums[i], nums[idx]
              
        res = []
        backtrack(0)
        return res 
        