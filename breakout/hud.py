
class HUD:
    def __init__(self):
        self.life = 3
        self.score = 0
        self.max_life = 3

    def consult_score_board(self):
        print(f"Vidas: {self.life}\n")
        print(f"Score: {self.score}\n")