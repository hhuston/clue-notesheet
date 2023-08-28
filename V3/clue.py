# Harrison Huston 
# August 2023

table = []
NUM_PLAYERS = 0
CARDS_PER_HAND = 0
CARDS = []
CARD_OPTIONS = ""

box_fillers = {-1: " ", 0 : "-", 1 : "X"}

def set_unowned(player, card):
    table[player][card] = 0
def set_owned(player, card):
    for i in range(NUM_PLAYERS):
        set_unowned(player, card)
    table[player][card] = 1

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
table = [["\t\t"] + CARDS] + [[players[x][0]] + [-1 for x in range (21)] + [0,0,0] for x in range(NUM_PLAYERS)]

for card in range(1, 22):
    if card in user_cards:
        set_owned(USER_INDEX, card)

#Get the Sidon Sum and Sidon Lists
# temp_list = [2*x for x in range(1,NUM_PLAYERS)]
# SIDON_SUM = pow(2, CARDS_PER_HAND + 1) - 2
# sidon_lists = []

for card in user_cards:
    set_owned(USER_INDEX, card)    

print_table()