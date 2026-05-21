class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # so here we create an array of frequencies
        freq = [[] for _ in range(len(nums) + 1)]
        cnt = defaultdict(int)
        for num in nums:
            cnt[num] += 1
        print(cnt, freq)
        for item in cnt.keys():
            freq[cnt[item]].append(item)
        
        res = []
        k_left = k
        for i in range(len(nums), -1, -1):
            if len(freq[i]) == 0:
                continue
            # take what we can
            cut = min(len(freq[i]), k_left)
            res += freq[i][:cut]
            k_left -= cut
        return res