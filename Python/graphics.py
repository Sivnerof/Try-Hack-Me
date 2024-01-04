"""Displays a ball's horizontal position on a screen."""

def show_screen(ball_position, screen_size):
    """Returns a graphical representation of the ball's position."""
    position = round(ball_position)

    # The position is offscreen so no ball is drawn.
    if position < 0 or position > screen_size:
        return "|" + (screen_size + 1) * " " + "|"

    spaces_before_ball = position * " "
    spaces_after_ball = (screen_size - position) * " "

    return "|" + spaces_before_ball + "o" + spaces_after_ball + "|"

