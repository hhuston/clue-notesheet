# Harrison Huston 
# August 2023

table = []
NUM_PLAYERS = 0
CARDS_PER_HAND = 0
CARDS = []
CARD_OPTIONS = ""

box_fillers = {0: " ", -1 : "-", 1 : "X"}

def set_unowned(player, card):
    table[player][card] = -1
    table[player][23] += 1
def set_owned(player, card):
    for others in range(1, NUM_PLAYERS + 1):
        set_unowned(others, card)
    table[player][card] = 1
    table[player][22] += 1

def print_table():
    notecard = "\n\n\n" + '=' * 18 + '=' * NUM_PLAYERS * 4 + "\n"
    for card in range(22):
        for player in range(NUM_PLAYERS + 1):
            box = table[player][card]
            if box in box_fillers:
                box = box_fillers[box]
            elif isinstance(box,int):
                box = "*"
            notecard += " | " + box
        notecard += " |\n"
        if card in [0, 6, 12, 21]:
            notecard += '=' * 18 + '=' * NUM_PLAYERS * 4 + "\n"
    print(notecard)
    


CARDS = ['Col. Mustard\t', 'Prof. Plum\t','Mr. Green\t', 'Mrs. Peacock\t', 'Miss Scarlet\t', 'Mrs. White\t', 
                   'Knife\t', 'Candlestick\t', 'Revolver\t', 'Rope\t\t', 'Lead Pipe\t', 'Wrench\t', 
                   'Hall\t\t', 'Lounge\t', 'Dining Room\t', 'Kitchen\t', 'Ballroom\t', 'Conservatory\t', 'Billiard Room', 'Library\t', 'Study\t']
CARD_OPTIONS = ("1 - " + CARDS[0] + ''   + "7  - " + CARDS[6]  + '\t'   + "13 - " + CARDS[12] + '\n' +
                "2 - " + CARDS[1] + '\t' + "8  - " + CARDS[7]  + ''   + "14 - " + CARDS[13] + '\n' +
                "3 - " + CARDS[2] + '\t' + "9  - " + CARDS[8]  + '\t' + "15 - " + CARDS[14] + '\n' +
                "4 - " + CARDS[3] + ''   + "10 - " + CARDS[9]  + ''   + "16 - " + CARDS[15] + '\n' +
                "5 - " + CARDS[4] + ''   + "11 - " + CARDS[10] + '\t' + "17 - " + CARDS[16] + '\n' +
                "6 - " + CARDS[5] + '\t' + "12 - " + CARDS[11] + '\t' + "18 - " + CARDS[17] + '\n' +
                '\t' * 6 + "19 - " + CARDS[18] + '\n' +
                '\t' * 6 + "20 - " + CARDS[19] + '\n' +
                '\t' * 6 + "21 - " + CARDS[20] + '\n')

print("-----------------------------------CLUE NOTESHEET-----------------------------------")
players = input("Enter the names of the players in order, with your name last, separated by spaces:\n\t")
players = [x.strip() for x in players.split(" ")]
NUM_PLAYERS = len(players)
USER_INDEX = NUM_PLAYERS

print()
print(CARD_OPTIONS)
user_cards = input("Enter the numbers of your cards, separated by spaces:\n\t")
user_cards = [int(x.strip()) for x in (user_cards.strip()).split(" ")]
CARDS_PER_HAND = len(user_cards)
communal_cards = input("Enter the numbers of the communal cards, separated by spaces. If there are none just press enter:\n\t")
if communal_cards != "":
    user_cards += [int(x.strip()) for x in (communal_cards.strip()).split(" ")]

# Build the table
table = [["\t\t"] + CARDS] + [[players[x][0]] + [0 for x in range (21)] + [0,0,2] for x in range(NUM_PLAYERS)]

for card in range(1, 22):
    if card in user_cards:
        set_owned(USER_INDEX, card)

#Get the Sidon Sum and Sidon Lists
# temp_list = [2*x for x in range(1,NUM_PLAYERS)]
# SIDON_SUM = pow(2, CARDS_PER_HAND + 1) - 2
# sidon_lists = []

for card in range(1,22):
    if card in user_cards:
        set_owned(USER_INDEX, card)  
    else:
        set_unowned(USER_INDEX, card)  

print("\n")
def print_players():
    for i in range(NUM_PLAYERS):
        print("\t" + str(i + 1) + " - " + players[i])

print_players()
guessing_player = int(input("\nEnter the number of the player who is going first:\n\t").strip())
eliminated_players = []
print("\n\n------------------------------------------------------------------------------------\n\n")

# Gameplay loop
while True:
    print_table()

    print("It is " + players[guessing_player - 1] + "'s turn to guess\n\n")
    print(CARD_OPTIONS)
    guessed_cards = input("Enter the cards that " + players[guessing_player - 1] + " guessed, separated by spaces:\n\t")
    guessed_cards = [int(card.strip()) for card in guessed_cards.strip().split(" ")]

    print()
    print_players()
    print("\t" + str(NUM_PLAYERS + 1) + " - No disprover\n")
    disprover = int(input("Enter the number of the person who disproved the guess:\n\t").strip())

    # If the player makes an accusation then the game either ends or they are removed from the guessing rotation
    if input("Is " + players[guessing_player - 1] + " making and accusation? (Y/N): \n\t").strip().upper() == "Y":
        if input("Was " + players[guessing_player - 1] + "'s accusation correct? (Y/N): \n\t").strip().upper() == "Y":
            print(players[guessing_player - 1] + " wins!")
            break
        else:
            eliminated_players += [guessing_player]

    # If no one could disprove the guess, set all the other players to not own any of the cards
    if disprover == NUM_PLAYERS + 1:
        for player in range(1, NUM_PLAYERS + 1):
            if player != disprover and player != USER_INDEX:
                for card in guessed_cards:
                    set_unowned(player, card)
    # If someone did disprove then set the people before the disprove as unowned for those cards
    else:
        temp = guessing_player
        while temp != disprover:
            if temp != USER_INDEX and temp != guessing_player:
                for card in guessed_cards:
                    set_unowned(temp, card)
            temp += 1
            if temp == NUM_PLAYERS:
                temp = 1
    
        # If you were the guesser you know what the shown card is
        if guessing_player == USER_INDEX and disprover != NUM_PLAYERS + 1:
            print(CARD_OPTIONS)
            set_owned(disprover, int(input("Enter the number of the card that you were shown:\n\t").strip()))
    
        # If you weren't the guesser and the disprover does not have one of the cards
        # then assign a number to each of the possible cards that were shown

        # When two of the cards guessed are known to be unowned by the disprover, they must own the third card
        if -2 == table[disprover][guessed_cards[0]] + table[disprover][guessed_cards[1]] + table[disprover][guessed_cards[2]]:
            for card in guessed_cards:
                if table[disprover][card] == 0:
                    set_owned(disprover, card)
        # If the disprover is not known to own any of the cards then add the next disproval level from the sidon set to their value
        elif table[disprover][guessed_cards[0]] != 1 and table[disprover][guessed_cards[1]] != 1 and table[disprover][guessed_cards[2]] != 1:
            for card in guessed_cards:
                if table[disprover][card] != -1:
                    table[disprover][card] += sidon_set[table[disprover][24]]
                    table[disprover][24] += 1
    
    # Start checking for deductions
    board_changed = [True] * NUM_PLAYERS + 1
    def board_was_changed(player):
        for i in range(1, NUM_PLAYERS + 1):
            if i != player:
                board_changed[i] = True
    
    checking_player = 1
    while True in board_changed:
        board_changed[checking_player] = False
        if table[checking_player][22] + table[checking_player][23] == 21:
            continue
        # Sidon set stuff

        # If all of the owned or unowned cards have been found, fill in the rest
        
        if table[checking_player][22] == 3:
            for card in range(1,22):
                if table[checking_player][card] == 0:
                    set_unowned(checking_player, card)
        elif table[checking_player][23] == 18:
            board_was_changed(checking_player)
            for card in range(1,22):
                if table[checking_player][card] == 0:
                    set_owned(checking_player, card)

