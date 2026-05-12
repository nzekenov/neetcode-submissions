
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for index, item in enumerate(strs):
            count = [0] * 26
            for character in item:
                count[ord(character) - ord('a')] += 1
            res[tuple(count)].append(item)
        return list(res.values())