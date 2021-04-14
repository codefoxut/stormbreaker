import time
from turtle import Screen

from paddle import Paddle
from ball import Ball
from scorecard import Scoreboard


class PongGame:
    def __init__(self):
        self.is_game_on = True
        self.move_speed = 0.5

    def stop(self):
        self.is_game_on = False

    def start(self):
        my_screen = self.get_screen()

        p_left = Paddle(-360)
        p_right = Paddle(360)

        ball = Ball()
        scoreboard = Scoreboard()

        my_screen.update()

        my_screen.listen()
        # left paddle move
        my_screen.onkey(p_left.up, key="w")
        my_screen.onkey(p_left.down, key="s")

        # right paddle
        my_screen.onkey(p_right.up, key="Up")
        my_screen.onkey(p_right.down, key="Down")

        my_screen.onkey(self.stop, key="space")

        while self.is_game_on:
            ball.move()
            if ball.touching_the_wall():
                ball.bounce_from_wall()

            if (
                p_left.distance(ball) < 50
                and ball.xcor() < -330
                and ball.moving_to == "left"
            ) or (
                p_right.distance(ball) < 50
                and ball.xcor() > 330
                and ball.moving_to == "right"
            ):
                ball.bounce_from_paddle()

            # left paddle
            if ball.xcor() < -360:
                ball.moving_to = "left"
                scoreboard.point_to_right()
                ball.reset_position()

            # right  paddle
            if ball.xcor() > 360:
                ball.moving_to = "right"
                scoreboard.point_to_left()
                ball.reset_position()

            my_screen.update()
            time.sleep(0.1)

        my_screen.exitonclick()

    @staticmethod
    def get_screen():
        screen = Screen()
        screen.setup(width=800, height=600)
        screen.bgcolor("black")
        screen.title("My Pong Game")
        screen.tracer(0)
        return screen


if __name__ == "__main__":
    PongGame().start()
