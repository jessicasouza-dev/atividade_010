# Press the green button in the gutter to run the script.
from paddle import Paddle
from ball import Ball
from hud import HUD
from wall import Wall

hud = HUD()
ball = Ball(hud)
wall = Wall(0, 700)
paddle = Paddle()
game_width = 1000
game_height = 1000
game_loop = True


def ball_coordinates():
    global ball, game_width, game_height, wall, paddle
    x = int(input("\nInsira o x: "))
    y = int(input("\nInsira o y: "))

    ball.x = x
    ball.y = y

    ball.collide_wall(wall)
    ball.collide_paddle(paddle)
    ball.collide_screen(game_width, game_height)


def update_game():
    global ball, hud, wall, paddle

    ball.consult_ball()
    hud.consult_score_board()
    wall.consult_wall()
    paddle.consult_paddle()


def menu():
    global ball, hud, wall, paddle, game_loop

    while game_loop and hud.life > 0:
        print("\nBREAKOUT\n")
        print("-------------\n")
        print("\n1 - Movimentar Paddle?")
        print("\n2 - Inserir coordenada para a Bola manualmente?")
        print("\n3 - Consultar estado do jogo?")
        print("\n4 - Consultar coordenadas dos blocos?")
        print("\n5 - Sair do jogo?")

        option = int(input("Escolha uma opção: "))

        if option == 1:
            paddle.paddle_movement()
        elif option == 2:
            ball_coordinates()
        elif option == 3:
            update_game()
        elif option == 4:
            wall.consult_bricks()
        elif option == 5:
            print("Obrigado por jogar!")
            game_loop = False

    if hud.life < 0:
        print("Você perdeu!")
    else:
        print("Obrigada por jogar")

if __name__ == '__main__':
    menu()

