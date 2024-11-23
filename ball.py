

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
            print("a bola colidiu com o player")
        else:
            print("a bola não colidiu com o player")

    def collide_wall(self, wall):
        collision = False
        for row in wall.wall:
            for brick in row:
                if self.x < brick.x + brick.width and self.x + self.width > brick.x and self.y < brick.y + brick.height and self.y + self.height > brick.y:
                    collision = True
                    self.dy *= -1
                    row.remove(brick)
                    self.hud.score += brick.score
                    print(f"\nBola colidiu com bloco no ponto ({self.x}, {self.y})!")
                    return



        if not collision:
            print("A bola não atingiu nenhum bloco")

    def collide_screen(self, game_width, game_height):
        if self.y > game_height:
            self.dy *= -1
            print("\nA bola atingiu o teto.")
        elif self.x > game_width:
            self.dx *= -1
            print("\nA bola atingiu as paredes.")
        elif self.y < 0:
            self.hud.life -= 1
            print("\nO jogador perdeu uma vida!")

            if self.hud.life == 0:
                print("\nO jogador perdeu!")
