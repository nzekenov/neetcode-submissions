class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hset = defaultdict(list)
        for s in strs:
            enc = [0] * 26
            for letter in s:
                idx = ord(letter) - ord('a')
                enc[idx] += 1
            hset[tuple(enc)].append(s)
        return list(hset.values())