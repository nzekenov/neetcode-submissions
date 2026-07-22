class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        st = []
        # print(sorted(zip(position, speed), key=lambda x:-x[0]))
        for x, v in sorted(zip(position, speed), key=lambda x:-x[0]):
            t = (target - x) / v
            if not st or t > st[-1]:   # arrives later than the fleet ahead → new fleet
                st.append(t)
        
        return len(st)