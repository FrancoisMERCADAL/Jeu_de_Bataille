import json

# open file and extract data
file_name = "dealings.json"
file = open(file_name)
data = json.load(file)

# get the dictionary keys
data_keys = list(data.keys())

# make 2 arrays for both players' cards
player1_cards = data[data_keys[0]]
player2_cards = data[data_keys[1]]

# define cards strengths and colors
cards_strengths_order = ["Two", "Three", "Four", "Five", "Six",
                         "Seven", "Eight", 'Nine', "Ten", "Jack", "Queen", "King", "Ace"]
cards_colors = {
    "Clubs": "Trèfle",
    "Diamonds": "Carreau",
    "Spades": "Pique",
    "Hearts": "Coeur"
}

# Start Game
player1_wins_count = 0
player2_wins_count = 0
count_turns = 0
while len(player1_cards) > 0 and len(player2_cards) > 0:
    count_turns += 1
    print(f"Turn {count_turns}")

    # Card played by each player
    # Each card is splitted into a list like ["value", "of", "color"]
    player1_card = player1_cards.pop(0).split(" ")
    player2_card = player2_cards.pop(0).split(" ")

    print(
        f"Player1 played {' '.join(player1_card)} \nPlayer2 played {' '.join(player2_card)}")

    # Details of each card
    player1_card_value = cards_strengths_order.index(player1_card[0])
    player1_card_color = player1_card[2]
    player2_card_value = cards_strengths_order.index(player2_card[0])
    player2_card_color = player2_card[2]

    # Decision
    victory_str = ""
    nb_winner = 0
    if player1_card_value < player2_card_value:
        nb_winner = 2
    elif player1_card_value > player2_card_value:
        nb_winner = 1
    elif player1_card_value == player2_card_value:
        print("BATTLE!!")
        # I thought about using an "elif" here but it would have made my "nb_winner = 1" redundant so I decided to use this 
        # super long if condition 
        if (cards_colors[player1_card_color] == "Pique" and cards_colors[player2_card_color] in ["Coeur", "Carreau"]) or (cards_colors[player1_card_color] == "Coeur" and cards_colors[player2_card_color] in ["Carreau", "Trèfle"]) or (cards_colors[player1_card_color] == "Carreau" and cards_colors[player2_card_color] == "Trèfle") or (cards_colors[player1_card_color] == "Trèfle" and cards_colors[player2_card_color] == "Pique"):
            nb_winner = 1
        else:
            nb_winner = 2

    # player1 wins case
    if nb_winner == 1:
        player1_wins_count += 1
        player1_cards.extend([' '.join(player1_card),' '.join(player2_card)])
    # player2 wins case
    elif nb_winner == 2:
        player2_wins_count += 1
        player2_cards.extend([' '.join(player2_card),' '.join(player1_card)])
    # error case
    else:
        raise ValueError('A problem occured')

    print(f"Player{nb_winner} wins")

print(
    f"End of the game: Player {nb_winner} wins the game \nPlayer1: {player1_wins_count} wins \nPlayer2: {player2_wins_count} wins")
