COLOR_RED = (255, 0, 0)
COLOR_ORANGE = (255, 165, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_YELLOW = (255, 255, 0)


from block import Block

class Wall:
    def __init__(self, x, y):
        super().__init__()
        self.wall = []
        self.collideable = True
        self.rows = 8
        self.columns = 14
        self.bricks = 0
        self.x = x
        self.y = y

        self.create_wall()

    def consult_wall(self):
        bricks = 0
        for row in self.wall:
            for brick in row:
                bricks += 1

        print(f"\nQuantidade de tijolos: {bricks}")

    def consult_bricks(self):
        for i, row in enumerate(self.wall):
            print(f"Row n.{i + 1}")
            for j, brick in enumerate(row):
                print(f"Block n.{j + 1}")
                brick.consult_brick()
    def create_wall(self):
        for i in range(self.rows):
            block_row = []
            for j in range(self.columns):
                brick_x = (j * (50 + 20)) + self.x
                brick_y = (i * (30 + 20)) + self.y
                if 0 <= i < 2:
                    brick_color = COLOR_RED
                    brick_points = 1
                    brick_speed = 4
                elif 2 <= i < 4:
                    brick_color = COLOR_ORANGE
                    brick_points = 2
                    brick_speed = 3
                elif 4 <= i < 6:
                    brick_color = COLOR_GREEN
                    brick_points = 3
                    brick_speed = 2
                else:
                    brick_color = COLOR_YELLOW
                    brick_points = 1
                    brick_speed = 1

                block_row.append(
                    Block(brick_x, brick_y, brick_points, brick_color, brick_speed))

            self.wall.append(block_row)



