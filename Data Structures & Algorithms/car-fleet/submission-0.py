class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p, s in zip(position, speed)]

        stack = []
        for p,s in sorted(pair)[::-1]:
            result = (target - p) / s
            stack.append(result)
            if len(stack) >=2  and stack[-1] <= stack[-2]: #current car is faster, so pop
                stack.pop()
            else:
                continue
        return len(stack)