"""Simulates a ball's movement and collision with the edges of a screen."""

def move(position, speed, right_wall):
    """Returns the ball's new position after one time step.
    The ball moves in straight line at the given speed.
    """
    left_wall = right_wall - right_wall
    if (position + speed) >= right_wall:
        return right_wall
    elif (position + speed) <= left_wall:
        return left_wall
    return position + speed

def maybe_bounce(position, speed, right_wall):
    """Returns the ball's new speed, which stays the same unless the ball
    bounces off of a wall.
    """
    left_wall = right_wall - right_wall
    if position >= right_wall:
        # Reverses direction and loses a bit of speed.
        speed = speed * -0.75
    elif position <= left_wall:
        # Reverses direction and loses a bit of speed.
        speed = speed * -0.75

    return speed

