class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = 0
        position_y = 0
        position_x = 0
        for ch in instructions:
            if ch == "G":
                if direction % 4 == 0:
                    position_y += 1
                elif direction % 4 == 1:
                    position_x += 1
                elif direction % 4 == 2:
                    position_y -= 1
                elif direction % 4 == 3:
                    position_x -= 1
            if ch == "L":
                direction -= 1
            elif ch == "R":
                direction += 1
        if direction % 4 == 0 and (position_x != 0 or position_y != 0):
            return False
        else:
            return True