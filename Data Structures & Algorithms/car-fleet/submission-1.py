class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = [[p, s] for p, s in zip(position, speed)]
        cars.sort()
        for position, speed in reversed(cars):
            time_to_reach_target = (target - position) / speed
            if not stack or stack[-1] < time_to_reach_target:
                stack.append(time_to_reach_target)
        return len(stack)

        