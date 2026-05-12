from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(nums, idx):
            if idx == len(nums):
                res.append(nums[:])
                return
            for i in range(idx, len(nums)):
                nums[idx], nums[i] = nums[i], nums[idx]
                backtrack(nums, idx + 1)
                nums[idx], nums[i] = nums[i], nums[idx]
              
        res = []
        backtrack(nums, 0)
        return res 
        