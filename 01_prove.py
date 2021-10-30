import random


def main():
    play_game()

def play_game():
    """The Game of Hilo is played in this function until the user quits or runs out of points"""

    playing = True
    points = 300

    while playing:
        card = generate_card()
        first_card_value = calc_card_value(card)
        print(f"The card is: {card}")
        user_guess = get_guess()

        next_card = generate_card()
        second_card_value = calc_card_value(next_card)
        print(f"Next card was: {next_card}")

        points = calculate_points(points,first_card_value, second_card_value, user_guess)
        print(f"Your score is: {points}")

        keep_playing = get_response()

        if game_done(points, keep_playing, message=True):
            playing = False



def calculate_points(points,first_card_value, second_card_value, user_guess):
    """Calculates how much points the user has after a guess"""
    
    if user_guess == "h" and (first_card_value < second_card_value):
        points += 100
    elif user_guess == "h" and (first_card_value > second_card_value):
        points -= 75
    elif user_guess == "l" and (first_card_value < second_card_value):
        points -= 75
    elif user_guess == "l" and (first_card_value > second_card_value):
        points += 100

    return points

def game_done(points, keep_playing, message=True):
    """Lets us know if the game is done. The conditions are if the user quits or runs out of points"""

    if points == 0:
        message = "You ran out of points. Game over." 
        print(message)
        return True
    
    if keep_playing == "n":
        message = "You are a Quitter!!!! Game over."
        print(message)
        return True

    return False

def generate_card():
    """Generates a random card from a list of cards to be used during the round"""

    list_of_cards = ['Ace',2,3,4,5,6,7,8,9,10,'Jack', 'Queen', 'King']
    new_card = random.choice(list_of_cards)
    return new_card

def calc_card_value(card):
    """Takes in a card and determines the value of that card"""

    sub_list = ['Ace','Jack','Queen','King']
    if card not in sub_list:
        card_value = card
    elif card == 'Ace':
        card_value = 1
    elif card == 'Jack':
        card_value = 11
    elif card == 'Queen':
        card_value = 12
    elif card == 'King':
        card_value = 13
    return card_value


def get_guess():
    """Gets input from the user for a guess of high or low in the form h or l"""

    getting_guess = True
    while getting_guess:
        try:
            guess = input("Higher or Lower? [h / l]: ")
            if guess.lower() == 'h' or guess.lower() == "l":
                getting_guess = False
            else:
                print("That was not one of the options. Try entering h or l")
        except ValueError:
            print("The type for this input is string.")

    return guess

def get_response():
    """Gets a response from the user for if they would like to keep playing"""

    getting_response = True
    while getting_response:
        try:
            response = input("Keep playing? [y / n]: ")
            if response.lower() == 'y' or response.lower() == "n":
                getting_response = False
            else:
                print("That was not one of the options. Try entering y or n")
        except ValueError:
            print("The type for this input is string.")
    return response


if __name__ == "__main__":
    main()