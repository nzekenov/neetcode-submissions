from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(map(list, list(permutations(nums, r = len(nums)))))