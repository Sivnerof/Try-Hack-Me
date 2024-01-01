def get_banana_score(num_bananas):
    """Returns a player's score based on the number of banana cards.
    Bananas are worth more in bunches.
    """
    if num_bananas == 1:
        return 1
    elif num_bananas == 2:
        return 4
    elif num_bananas >= 3:
        return 10
    else:
        return 0

def get_apple_score(num_apples, has_poison_apple):
    """Returns a player's score based on the number of apple cards.
    The poison apple card turns the apple score negative.
    """
    if has_poison_apple:
        return num_apples * -2
    else:
        return num_apples * 2

def get_score(bananas, apples, has_poison_apple, cherries):
    """Returns a player's total score based on their cards of each type."""
    banana_score = get_banana_score(bananas)
    apple_score = get_apple_score(apples, has_poison_apple)
    cherry_score = get_cherry_score(cherries)
    
    return banana_score + apple_score + cherry_score

def get_cherry_score(cherry_cards):
    return cherry_cards // 2 * 5

# Calculate the final score for each player.
player1_score = get_score(3, 2, True, 3)
player2_score = get_score(1, 5, False, 4)
print("Scores: p1=" + str(player1_score) + ", p2=" + str(player2_score))

