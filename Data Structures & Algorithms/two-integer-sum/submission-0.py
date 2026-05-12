from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memory = defaultdict(int)
        for index, item in enumerate(nums):
            if target - item in memory:
                return [memory.get(target-item), index]
            else:
                memory[item] = index
        return None