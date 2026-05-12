class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hset = {}
        for index, num in enumerate(nums):
            idx = hset.get(target-num, -1)
            if idx != -1:
                return [idx, index]
            hset[num] = index
        return []