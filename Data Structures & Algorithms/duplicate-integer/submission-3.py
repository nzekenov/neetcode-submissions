class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hmap = defaultdict(bool)
        # for num in nums:
        #     if hmap[num]:
        #         return True
        #     hmap[num] = True
        # return False
        visited = set(nums)

        return len(visited) != len(nums)