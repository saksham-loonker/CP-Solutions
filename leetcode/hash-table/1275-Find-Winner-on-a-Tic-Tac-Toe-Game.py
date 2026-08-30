class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = []
        for _ in range(3):
            row = ["", "", ""]
            board.append(row)

        turn = 0
        for r, c in moves:
            if turn==0:
                board[r][c] = "X"
            else:
                board[r][c] = "O"
            if turn == 0:
               turn = 1
            elif turn == 1:
                turn = 0

        for i in range(3):
            if board[i][0] and board[i][0] == board[i][1] == board[i][2]:
                if board[i][0] == "X":
                    return "A"
                else:
                    return "B"
            if board[0][i] and board[0][i] == board[1][i] == board[2][i]:
                if board[0][i] == "X":
                    return "A"
                else:
                    return "B"
        if board[1][1] and ((board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0])):
            if board[1][1] == "X":
                return "A"
            else:
                return "B"
        if len(moves)==9:
            return "Draw"
        else:
            return "Pending"