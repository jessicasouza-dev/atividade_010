class Paddle:
    def __init__(self):
        self.width = 150
        self.height = 50
        self.x = 0
        self.y = 800
        self.direction = "neutral"
        self.speed = 5

    def consult_paddle(self):
        print(f"Posição do Paddle: ({self.x}, {self.y})")
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
            while direction != 1 and direction != 2:
                print("\nResposta inválida!")
                print("\n1 - Direita")
                print("\n2 - Esquerda")
                direction = int(input("Qual direção deseja ir: "))

            if direction == 1:
                self.direction = "right"
            elif direction == 2:
                self.direction = "left"

        print("\nInício do movimento!")
        self.consult_paddle()

        self.paddle_check()

        print("\nFim do movimento!")
        self.consult_paddle()



    def paddle_check(self):

        if self.direction == "neutral" and 0 <= self.x + 0 <= 1000:
            self.speed = 0
            self.x = self.x + self.speed

        elif self.direction == "right" and 0 <= self.x + 5 <= 1000:
            self.speed = 5
            self.x = self.x + self.speed

        elif self.direction == "left" and 0 <= self.x - 5 <= 1000:
            self.speed = -5
            self.x = self.x + self.speed

        elif self.x + 5 < 0 or self.x + 5 > 1000 or self.x - 5 < 5 or self.x - 5 > 1000:
            print("O Paddle bateu na parede!")

        else:
            print("Direçao inválida!")
