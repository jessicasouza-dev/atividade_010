
class HUD:
    def __init__(self):
        self.score_player1 = 0
        self.score_player2 = 0
        self.max_score = 3

    def consult_score_board(self):
        print(f"Player 1: {self.score_player1}\n")
        print(f"Player 2: {self.score_player2}\n")