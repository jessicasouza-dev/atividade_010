
class Block:
    def __init__(self, x, y, score, color, speed):
        self.score = score
        self.width = 50
        self.height = 50
        self.x = x
        self. y = y
        self.color = color
        self.speed = speed


    def consult_brick(self):
        print(f"Cor do bloco: {self.color}")
        print(f"X do bloco: {self.x}")
        print(f"Y do bloco: {self.y}")
        print(f"Score do bloco: {self.score}")