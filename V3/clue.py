cards = ['Col. Mustard\t', 'Prof. Plum\t','Mr. Green\t', 'Mrs. Peacock\t', 'Miss Scarlet\t', 'Mrs. White\t', 
                   'Knife\t\t', 'Candlestick\t', 'Revolver\t', 'Rope\t\t', 'Lead Pipe\t', 'Wrench\t', 
                   'Hall\t\t', 'Lounge\t', 'Dining Room\t', 'Kitchen\t', 'Ballroom\t', 'Conservatory\t', 'Billiard Room\t', 'Library\t', 'Study\t\t']
card_options = ("1 - " + cards[0] + ''   + "7  - " + cards[6]  + ''   + "13 - " + cards[12] + '\n' +
                "2 - " + cards[1] + '\t' + "8  - " + cards[7]  + ''   + "14 - " + cards[13] + '\n' +
                "3 - " + cards[2] + '\t' + "9  - " + cards[8]  + '\t' + "15 - " + cards[14] + '\n' +
                "4 - " + cards[3] + ''   + "10 - " + cards[9]  + ''   + "16 - " + cards[15] + '\n' +
                "5 - " + cards[4] + ''   + "11 - " + cards[10] + '\t' + "17 - " + cards[16] + '\n' +
                "6 - " + cards[5] + '\t' + "12 - " + cards[11] + '\t' + "18 - " + cards[17] + '\n' +
                '\t' * 6 + "19 - " + cards[18] + '\n' +
                '\t' * 6 + "20 - " + cards[19] + '\n' +
                '\t' * 6 + "21 - " + cards[20] + '\n')

print("-----------------------------------CLUE NOTESHEET-----------------------------------")
players = input("Enter the names of the players in order, with your name last, separated by spaces:\n\t")
players = [x.strip() for x in players.split(" ")]
NUM_PLAYERS = len(players)

print()
print(card_options)
user_cards = input("Enter the numbers of your cards, separated by spaces:\n\t")
user_cards = [int(x.strip()) for x in user_cards.split(" ")]
CARDS_PER_HAND = len(user_cards)
communal_cards = input("Enter the numbers of the communal cards, separated by spaces. If none just press enter:\n\t")
user_cards += [int(x.strip()) for x in communal_cards.split(" ")]

#Get the Sidon Sum and Sidon Lists
temp_list = [2*x for x in range(1,NUM_PLAYERS)]
SIDON_SUM = pow(2, CARDS_PER_HAND + 1) - 2
sidon_lists = []
for i in range(CARDS_PER_HAND):

# Example Sidon lists for 1 cards per hand
# [[2]]
     
# Example Sidon lists for 2 cards per hand
# [[2, 6], [4, 6]]

# Example Sidon lists for 3 cards per hand
# [[2, 6, 10, 14], [4, 6, 12, 14], [8, 10, 12, 14]]
# Rewrite
# [[(14 - 8 - 4), (14 - 8), (14 - 4), 14], 
# [(14 - 8 - 2), (14 - 8), (14 - 2), 14],
# [(14 - 4 - 2), (14 - 4), (14 - 2), 14]]

# Example Sidon lists for 4 cards per hand
# [[2, 6, 10, 14, 18, 22, 26, 30], [4, 6, 12, 14, 20, 22, 28, 30],
#  [8, 10, 12, 14, 24, 26, 28, 30], [16, 18, 20, 24, 26, 28, 30]]
# Rewrite
# [[(30 - 16 - 8 - 4), (30 - 16 - 8), (30 - 16 - 4), (30 - 16), (30 - 8 - 4), (30 - 8), (30 - 4), 30]]