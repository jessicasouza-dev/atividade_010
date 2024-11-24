# Press the green button in the gutter to run the script.
from paddle import Paddle
from ball import Ball
from hud import HUD

game_width = 800
game_height = 600
game_loop = True
hud = HUD()
ball = Ball(hud)
player1 = Paddle(60, game_height//2, 1)
player2 = Paddle(game_width - 60, game_height//2, 2)

def ball_coordinates():
    global ball, game_width, game_height, player1, player2
    x = int(input("\nInsira o x: "))
    y = int(input("\nInsira o y: "))

    ball.x = x
    ball.y = y

    ball.collide_paddle(player1)
    ball.collide_paddle(player2)
    ball.collide_screen(game_width, game_height)


def update_game():
    global ball, hud, player1, player2

    ball.consult_ball()
    hud.consult_score_board()
    player1.consult_paddle()
    player2.consult_paddle()


def menu():
    global ball, hud, player1, player2, game_loop, game_height

    while game_loop:
        print("\nPONG\n")
        print("-------------\n")
        print("\n1 - Movimentar Jogador 1?")
        print("\n2 - Movimentar Jogador 2?")
        print("\n3 - Inserir coordenada para a Bola manualmente?")
        print("\n4 - Consultar estado do jogo?")
        print("\n5 - Sair do jogo?")

        option = int(input("Escolha uma opção: "))

        if option == 1:
            player1.paddle_movement(game_height)
        elif option == 2:
            player2.paddle_movement(game_height)
        elif option == 3:
            ball_coordinates()
        elif option == 4:
            update_game()
        elif option == 5:
            print("Obrigado por jogar!")
            game_loop = False

        if hud.score_player1 == 3:
            print("Jogador 1 VENCEU!")
            game_loop = False
        elif hud.score_player2 == 3:
            print("Jogador 2 VENCEU!")
            game_loop = False

if __name__ == '__main__':
    menu()

