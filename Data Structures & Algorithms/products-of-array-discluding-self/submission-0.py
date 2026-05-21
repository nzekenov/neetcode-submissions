class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # one array is product from left to right
        # other array is product from right to left
        lr = [1]
        for i in range(len(nums)):
            lr.append(lr[i] * nums[i])
        rl = [1]
        for i in range(len(nums)):
            rl.append(rl[i] * nums[len(nums) - 1 - i])
        res = []
        for i in range(1, len(nums) + 1):
            curr = lr[i-1] * rl[-1-i]
            res.append(curr)

        return res