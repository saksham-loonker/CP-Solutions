class Solution:
    def judgeCircle(self, moves: str) -> bool:
        position_x = 0
        position_y = 0
        for ch in moves:
            if ch == "U":
                position_y += 1
            elif ch == "D":
                position_y -= 1
            elif ch == "L":
                position_x -= 1
            elif ch == "R":
                position_x += 1
        if position_x == 0 and position_y == 0:
            return True
        else:
            return False

