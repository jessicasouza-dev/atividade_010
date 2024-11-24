
class Paddle:
    def __init__(self):
        self.width = 150
        self.height = 50
        self.x = 0
        self.y = 0
        self.direction = "neutral"
        self.speed = 15

    def consult_paddle(self):
        print(f"Posição do Paddle: ({self.x }, {self.y})")
        print(f"Direção do Paddle: {self.direction}")

    def paddle_movement(self):
        print("\n1 - Direita")
        print("\n2 - Esquerda")
        direction = int(input("Qual direção deseja ir: "))

        if direction == 1:
            self.direction = "right"
        elif direction == 2:
            self.direction = "left"
        else:
            while direction != 1 and direction !=2:
                print("\nResposta inválida!")
                print("\n1 - Direita")
                print("\n2 - Esquerda")
                direction = int(input("Qual direção deseja ir: "))

        print("\nInício do movimento!")
        self.consult_paddle()

        self.paddle_check()
        self.x = self.x + self.speed

        print("\nFim do movimento!")
        self.consult_paddle()



    def paddle_check(self):
        if self.direction == "neutral":
            self.speed = 0

        elif self.direction == "right":
            self.speed = 5

        elif self.direction == "left":
            self.speed = -5
        else:
            print("Direção inválida!")