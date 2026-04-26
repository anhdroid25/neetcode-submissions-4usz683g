class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        order_desc = list(zip(position, speed))
        order_desc.sort(reverse=True)

        prev_time = 0 
        fleet = 0

        for pos, spd in order_desc:
            equation = (target - pos) / float(spd)
            if equation > prev_time :
                fleet += 1
                prev_time = equation
        return fleet