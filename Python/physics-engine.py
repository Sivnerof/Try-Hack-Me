import ball
import graphics

output_width = 19
ball_position = 1
ball_speed = 5

for time_step in range(100):
    # Show the ball's position at the current time step.
    print(graphics.show_screen(ball_position, output_width))
    ball_position = ball.move(ball_position, ball_speed, output_width)
    ball_speed = ball.maybe_bounce(ball_position, ball_speed, output_width)

