import time
from turtle import Screen

from food import Food
from scorecard import ScoreCard
from snake import Snake


class SnakeGame:
    def __init__(self):
        self.screen = None

    @staticmethod
    def get_screen():
        screen = Screen()
        screen.setup(width=600, height=600)
        screen.bgcolor("black")
        screen.title("My Snake Game")
        screen.tracer(0)
        screen.register_shape(
            "snake_piece", ((10, 10), (10, -10), (-10, -10), (-10, 10))
        )
        return screen

    def start(self):
        is_game_on = True
        self.screen = self.get_screen()
        snake = Snake()
        food = Food()
        food.next_position(snake)
        scorecard = ScoreCard()
        self.screen.update()
        self.screen.listen()
        # self.screen.onkey(key="w", fun=self.move_forward)
        # self.screen.onkey(key="s", fun=move_backward)
        self.screen.onkey(key="a", fun=snake.move_anticlockwise)
        self.screen.onkey(key="d", fun=snake.move_clockwise)
        self.screen.onkey(key="Up", fun=snake.up)
        self.screen.onkey(key="Down", fun=snake.down)
        self.screen.onkey(key="Left", fun=snake.left)
        self.screen.onkey(key="Right", fun=snake.right)

        while is_game_on:
            snake.move()
            self.screen.update()
            time.sleep(0.1)

            # detect collision with food
            # print(snake.head.distance(food))
            if snake.head.distance(food) < 15:
                scorecard.update_score()
                food.next_position(snake)
                snake.extend()

            if snake.hit_the_wall() or snake.hit_the_tail():
                scorecard.game_over()
                is_game_on = False

        self.screen.exitonclick()


if __name__ == "__main__":
    SnakeGame().start()
