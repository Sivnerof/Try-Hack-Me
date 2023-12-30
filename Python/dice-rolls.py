import random

rolls = int(input("Repeat how many times? "))
roll_total = 0
rolls_copy = rolls

while rolls >= 1:
    # Roll two six-sided dice.
    first_die = random.randint(1, 6)
    second_die = random.randint(1, 6)

    dice_sum = first_die + second_die

    roll_total += dice_sum
    
    print("You rolled a " + str(dice_sum) + "!")
    rolls = rolls - 1

print("Roll total is: " + str(roll_total))
print("Roll average is: " + str(roll_total / rolls_copy))

