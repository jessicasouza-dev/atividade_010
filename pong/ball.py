

class Ball:
    def __init__(self, hud):
        self.width = 150
        self.height = 50
        self.x = 0
        self.y = 0
        self.dx = 5
        self.dy = 5
        self.hud = hud

    def consult_ball(self):
        print(f"\n Posição da bola: ({self.x + self.width}, {self.y + self.height})")
        print(f"\n Velocidade y da bola: {self.dy}")
        print(f"\n Velocidade x da bola: {self.dx}")

        if self.dy > 0:
            print("\nA bola está indo para cima")
        else:
            print("\nA bola está indo para baixo")

        if self.dx > 0:
            print("\nA bola está indo para a direita")
        else:
            print("\nA bola está indo para a esquerda")

    def ball_movement(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy

    def collide_paddle(self, paddle):
        if self.x < paddle.x + paddle.width and self.x + self.width > paddle.x and self.y + self.height >= paddle.y and self.y <= paddle.y + paddle.height:
            self.dy *= -1
            print(f"a bola colidiu com o player {paddle.player}")
        else:
            print(f"a bola não colidiu com o player{paddle.player}")


    def collide_screen(self, game_width, game_height):
        if self.y < 0:
            self.dy *= -1
            print("\nA bola atingiu a parede superior.")
        elif self.y > game_height:
            self.dy *= -1
            print("\nA bola atingiu a parede inferior.")
        elif self.x > game_width:
            self.hud.score_player1 += 1
            print("\nO jogador 1 marcou um ponto!")
        elif self.x < 0:
            self.hud.score_player2 += 1
            print("\nO jogador 2 marcou um ponto!")
