class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def helper(subnums):
            if not subnums:
                return 0
            
            n = len(subnums)
            if n == 1:
                return subnums[0]
            dp = [0] * n
            dp[0] = subnums[0]
            dp[1] = max(subnums[0], subnums[1])

            for i in range(2, n):
                dp[i] = max(dp[i - 1], subnums[i] + dp[i - 2])
            return dp[-1]
        return max(helper(nums[1:]), helper(nums[:-1]))