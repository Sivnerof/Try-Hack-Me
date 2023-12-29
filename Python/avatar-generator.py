import avatar
import random


random_number_bow = random.randint(1, 3)
random_number_nose = random.randint(1, 2)
random_number_mouth = random.randint(1, 4)

if random_number_bow == 1:
    avatar.draw_bow()

avatar.draw_eyes("medium")

if random_number_nose == 1:
    avatar.draw_nose("triangle")
else:
    avatar.draw_nose("button")

if random_number_mouth == 1 or random_number_mouth == 2:
    avatar.draw_mouth("smile")
elif random_number_mouth == 3:
    avatar.draw_mouth("teeth")
else:
    avatar.draw_mouth("neutral")

if random_number_bow == 3:
    avatar.draw_bow()

