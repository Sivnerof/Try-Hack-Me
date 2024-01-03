import round

user_score = 0
computer_score = 0

# The first player to win two rounds wins the game.
while user_score < 2 and computer_score < 2:
    user_choice = round.make_user_choice()
    computer_choice = round.make_computer_choice()
    print(user_choice + " (you) vs. " + computer_choice)

    # Restart the round if both players choose the same thing.
    if user_choice == computer_choice:
        print("It's a tie!")
        continue

    if round.wins_matchup(user_choice, computer_choice):
        print("You win!")
        user_score = user_score + 1
    else:
        print("Computer wins!")
        computer_score = computer_score + 1

    print(round.format_score(user_score, computer_score))

