class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        st = []
        for curr, temp in enumerate(temperatures):
            while len(st) > 0 and temp > st[-1][0]:
                _, idx = st.pop()
                res[idx] = (curr - idx)
            st.append((temp, curr))
        return res