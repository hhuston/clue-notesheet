# Harrison Huston 
# August 2023

table = []
NUM_PLAYERS = 0
CARDS_PER_HAND = 0
CARDS = []
CARD_OPTIONS = ""

box_fillers = {0: " ", -1 : "-", 1 : "X"}

def set_unowned(player, card):
    if table[player][card] != -1:
        table[player][card] = -1
        table[player][23] += 1
def set_owned(player, card):
    for others in range(1, NUM_PLAYERS + 1):
        if others != player:
            set_unowned(others, card)
    if table[player][card] != 1:
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
while True:
    user_cards = input("Enter the numbers of your cards, separated by spaces:\n\t")
    try:
        user_cards = [int(x.strip()) for x in (user_cards.strip()).split(" ")]
    except:
        print("Please enter only numbers and spaces\n")
    else:
        break

CARDS_PER_HAND = len(user_cards)
while True:
    communal_cards = input("Enter the numbers of the communal cards, separated by spaces. If there are none just press enter:\n\t")
    if communal_cards != "":
        try:
            user_cards += [int(x.strip()) for x in (communal_cards.strip()).split(" ")]
        except:
            print("Please only enter numbers and spaces\n")
        else:
            break
    else:
        break
    

# Build the table
table = [["\t\t"] + CARDS] + [[players[x][0]] + [0 for x in range (21)] + [0,0,-1] for x in range(NUM_PLAYERS)]

for card in range(1, 22):
    if card in user_cards:
        set_owned(USER_INDEX, card)

sidon_set = [2,3,4,8]
sidon_lists = [[2,5,6,10,9,13,14,17], [3,5,7,9,11,13,15,17], [4,6,7,12,9,14,15,17], [8,10,11,12,13,14,15,17]]

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
guessing_player = 0
while True:
    try:
        guessing_player = int(input("\nEnter the number of the player who is going first:\n\t").strip())
    except:
        print("Please enter a number\n")
    else:
        if guessing_player > 0 and guessing_player <= USER_INDEX:
            break
        else:
            print("The number you entered is out of range")

eliminated_players = []
print("\n\n------------------------------------------------------------------------------------\n\n")

answer = [0,0,0]

# Gameplay loop
while True:
    print_table()
    if 0 not in answer:
        print("It was " + table[0][answer[0]] + " with the " + table[0][answer[1]] + " in the " + table[0][answer[2]])

    print("It is " + players[guessing_player - 1] + "'s turn to guess\n\n")        
    print(CARD_OPTIONS)
    guessed_cards = input("Enter the cards that " + players[guessing_player - 1] + " guessed, separated by spaces. Enter 0 if they did not guess:\n\t")
    guessed_cards = [int(card.strip()) for card in guessed_cards.strip().split(" ")]
    if guessed_cards[0] == 0:
        guessing_player += 1
        if guessing_player in eliminated_players:
            guessing_player += 1
        if guessing_player > NUM_PLAYERS:
            guessing_player = 1
        continue

    print()
    print_players()
    print("\t" + str(NUM_PLAYERS + 1) + " - No disprover\n\t" + str(NUM_PLAYERS + 2) + " - " + players[guessing_player - 1] + " is making an accusation")
    while True:
        try:
            disprover = int(input("Enter the number of the person who disproved the guess:\n\t").strip())
        except:
            print("Please enter a number\n")
        else:
            if guessing_player > 0 and guessing_player <= NUM_PLAYERS + 2:
                break
            else:
                print("The number you entered is out of range")

    # If the player makes an accusation then the game either ends or they are removed from the guessing rotation
    if disprover == NUM_PLAYERS + 2:
        if input("Was " + players[guessing_player - 1] + "'s accusation correct? (Y/N): \n\t").strip().upper() == "Y":
            print(players[guessing_player - 1] + " wins!")
            break
        else:
            eliminated_players += [guessing_player]
            guessing_player += 1
            if guessing_player in eliminated_players:
                guessing_player += 1
            if guessing_player > NUM_PLAYERS:
                guessing_player = 1
            continue

    # If no one could disprove the guess, set all the other players to not own any of the cards
    if disprover == NUM_PLAYERS + 1:
        for player in range(1, NUM_PLAYERS + 1):
            if player != guessing_player and player != USER_INDEX:
                for card in guessed_cards:
                    set_unowned(player, card)
    # If someone did disprove then set the people before the disprove as unowned for those cards
    else:
        skipped_player = guessing_player + 1
        while skipped_player != disprover:
            if skipped_player >= USER_INDEX:
                skipped_player = 1
                continue
            for card in guessed_cards:
                set_unowned(skipped_player, card)
            skipped_player += 1
    
        # If you were the guesser you know what the shown card is
        if guessing_player == USER_INDEX and disprover != NUM_PLAYERS + 1:
            print(CARD_OPTIONS)
            while True: 
                try:
                    shown_card = int(input("Enter the number of the card that you were shown:\n\t").strip())
                except:
                    print("Please enter a number")
                else:
                    if shown_card > 0 and shown_card < 22:
                        set_owned(disprover, shown_card)
                        break
                    else:
                        print("The number you entered is out of range")
    
        # If you weren't the guesser and the disprover does not have one of the cards
        # then assign a number to each of the possible cards that were shown

        # When two of the cards guessed are known to be unowned by the disprover, they must own the third card
        if -2 == table[disprover][guessed_cards[0]] + table[disprover][guessed_cards[1]] + table[disprover][guessed_cards[2]]:
            for card in guessed_cards:
                if table[disprover][card] == 0:
                    set_owned(disprover, card)
        # If the disprover is not known to own any of the cards then add the next disproval level from the sidon set to their value
        elif table[disprover][guessed_cards[0]] != 1 and table[disprover][guessed_cards[1]] != 1 and table[disprover][guessed_cards[2]] != 1:
            table[disprover][24] += 1
            for card in guessed_cards:
                if table[disprover][card] != -1:
                    table[disprover][card] += sidon_set[table[disprover][24]]
            
    
    # Start checking for deductions
    board_changed = [False] + [True] * (NUM_PLAYERS -1)
    def board_was_changed(player):
        for i in range(1, NUM_PLAYERS):
            if i != player:
                board_changed[i] = True
    
    checking_player = 1
    while True in board_changed:
        if table[checking_player][22] + table[checking_player][23] == 21 or board_changed[checking_player] == False:
            board_changed[checking_player] = False
            checking_player += 1
            if checking_player == USER_INDEX:
                checking_player = 1
            continue

        board_changed[checking_player] = False

        # Sidon set stuff
        if table[checking_player][24] != -1:
            disprovals = [[]] * (table[checking_player][24] + 1)
            # Start by looping through the cards and adding them to their corresponding disproval groups
            # Then check if any of the groups only has one card in it
            # Save that card's number and see if it is in any other group
            # If it is then subtract that group's value from all of those cards
            # Set the saved card to owned and call board_was_changed()
            for i in range(len(disprovals)):
                for card in range(1,22):
                    if table[checking_player][card] in sidon_lists[i]:
                        disprovals[i] += [card]
            for i in range(len(disprovals)):
                if len(disprovals[i]) == 1:
                    owned_card = disprovals[i][0]
                    for j in range(len(disprovals)):
                        if table[checking_player][owned_card] in sidon_lists[j]:
                            map(lambda x: table[checking_player][x] - sidon_set[j], sidon_lists[j])
                            sidon_lists[j] = []
                    set_owned(checking_player, owned_card)
                    board_was_changed(checking_player)
                

        # If all of a player's owned or unowned cards have been found, fill in the rest
        if table[checking_player][22] == CARDS_PER_HAND:
            for card in range(1,22):
                if table[checking_player][card] == 0:
                    set_unowned(checking_player, card)
        elif table[checking_player][23] == 21 - CARDS_PER_HAND:
            board_was_changed(checking_player)
            for card in range(1,22):
                if table[checking_player][card] == 0:
                    set_owned(checking_player, card)

        checking_player += 1
        if checking_player == USER_INDEX:
            checking_player = 1


    # Check if the answer is found
    # Person
    if answer[0] == 0:
        player_answer = []
        for card in range(1, 7):
            owned = False
            card_sum = 0
            for player in range(1, NUM_PLAYERS + 1):
                if table[player][card] == 1:
                    owned = True
                card_sum += table[player][card]
            if not owned:
                player_answer += [card]
            if card_sum == NUM_PLAYERS * -1:
                answer[0] = card
        if answer[0] == 0 and len(player_answer) == 1:
            answer[0] = player_answer[0]
    if answer[1] == 0:
        weapon_answer = []
        for card in range(7, 13):
            owned = False
            card_sum = 0
            for player in range(1, NUM_PLAYERS + 1):
                if table[player][card] == 1:
                    owned = True
                card_sum += table[player][card]
            if not owned:
                weapon_answer += [card]
            if card_sum == NUM_PLAYERS * -1:
                answer[1] = card
        if answer[1] == 0 and len(weapon_answer) == 1:
            answer[1] = weapon_answer[0]
    if answer[2] == 0:
        room_answer = []
        for card in range(13, 22):
            owned = False
            card_sum = 0
            for player in range(1, NUM_PLAYERS + 1):
                if table[player][card] == 1:
                    owned = True
                card_sum += table[player][card]
            if not owned:
                room_answer += [card]
            if card_sum == NUM_PLAYERS * -1:
                answer[2] = card
        if answer[2] == 0 and len(room_answer) == 1:
            answer[2] = room_answer[0]

    guessing_player += 1
    if guessing_player in eliminated_players:
        guessing_player += 1
    if guessing_player > NUM_PLAYERS:
        guessing_player = 1