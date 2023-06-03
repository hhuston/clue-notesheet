from V2.Player import Player

class Game:

    def __init__(self):
        global Players
        global cards

        Players = []
        cards = ['Col. Mustard\t', 'Prof. Plum\t','Mr. Green\t', 'Mrs. Peacock\t', 'Miss Scarlet\t', 'Mrs. White\t', 
                   'Knife\t\t', 'Candlestick\t', 'Revolver\t', 'Rope\t\t', 'Lead Pipe\t', 'Wrench\t', 
                   'Hall\t\t', 'Lounge\t', 'Dining Room\t', 'Kitchen\t', 'Ballroom\t', 'Conservatory\t', 'Billiard Room\t', 'Library\t', 'Study\t\t']
    
    def get_players(self) -> None:
        global Players
        global num_players
        global card_owners

        names = input("Enter the names of players in order, with yourself last, separated by spaces:\n\t")
        print()
        names = names.strip().split(' ')
        # Add some error checking eventually
        num_players = len(names)
        for i in range(num_players):
            Players += [Player(names[i])]
        card_owners = [num_players for x in range(21)]
    
    def set_user_cards(self) -> None:
        global CARDS_PER_HAND

        print(self.print_cards())
        user_cards = input('Enter the numbers of your cards, separated by sapces:\n\t')
        print()
        user_cards = list(map(lambda x: int(x), user_cards.strip().split(' ')))
        CARDS_PER_HAND = len(user_cards)
        for card in user_cards:
            self.set_card_onwer(card, num_players - 1)
            for p in Players[:-1]:
                p.set_unowned(card)

    def set_card_owner(self, card : int, owner : int) -> None:
        global Players
        global card_owners

        card_owners[card] = 1
        Players[owner].set_owned(card)
        for i in range(num_players - 1):
            if i != owner:
                Players[i].set_unowned(card)    

    def print_cards(self) -> str:
        return ("1 - " + cards[0] + ''   + "7  - " + cards[6]  + ''   + "13 - " + cards[12] + '\n' +
                "2 - " + cards[1] + '\t' + "8  - " + cards[7]  + ''   + "14 - " + cards[13] + '\n' +
                "3 - " + cards[2] + '\t' + "9  - " + cards[8]  + '\t' + "15 - " + cards[14] + '\n' +
                "4 - " + cards[3] + ''   + "10 - " + cards[9]  + ''   + "16 - " + cards[15] + '\n' +
                "5 - " + cards[4] + ''   + "11 - " + cards[10] + '\t' + "17 - " + cards[16] + '\n' +
                "6 - " + cards[5] + '\t' + "12 - " + cards[11] + '\t' + "18 - " + cards[17] + '\n' +
                '\t' * 6 + "19 - " + cards[18] + '\n' +
                '\t' * 6 + "20 - " + cards[19] + '\n' +
                '\t' * 6 + "21 - " + cards[20] + '\n')

if __name__ == "__main__":
    G = Game()
    G.get_players()
    G.set_user_cards()