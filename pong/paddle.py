
class Paddle:
    def __init__(self, paddle_x, paddle_y,player):
        self.width = 50
        self.height = 150
        self.x = paddle_x
        self.y = paddle_y
        self.direction = "neutral"
        self.speed = 15
        self.player = player

    def consult_paddle(self):
        print(f"Posição do Player {self.player}: ({self.x }, {self.y})")
        print(f"Direção do Player {self.player}: {self.direction}")

    def paddle_movement(self,screen_height):
        print("\n1 - Cima")
        print("\n2 - Baixo")
        direction = int(input("Qual direção deseja ir: "))

        if direction == 1:
            self.direction = "up"
        elif direction == 2:
            self.direction = "down"
        else:
            while direction != 1 and direction !=2:
                print("\nResposta inválida!")
                print("\n1 - Cima")
                print("\n2 - Baixo")
                direction = int(input("Qual direção deseja ir: "))

        print("\nInício do movimento!")
        self.consult_paddle()

        if self.paddle_check(screen_height):
            self.y = self.y + self.speed

        print("\nFim do movimento!")
        self.consult_paddle()



    def paddle_check(self,screen_height):
        if self.direction == "neutral":
            self.speed = 0
            return True
        elif self.direction == "up":
            if self.y - 5 >= 0:
                self.speed = - 15
                return True
            else:
                print(f'O player {self.player} atingiu o teto.')
                return False
        elif self.direction == "down":
            if self.y + self.height + 5 <= screen_height:
                self.speed = 15
                return True
            else:
                print(f'O player {self.player} atingiu o chão.')
                return False
        else:
            print("Direção inválida!")
            return False