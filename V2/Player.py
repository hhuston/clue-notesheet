class Player:

    def __init__(self, n : str) -> None:
        global name
        global owned_cards
        global unowned_cards
        global cards

        self.name = n
        self.owned_cards = 0
        self.unowned_cards = 0
        self.cards = [0 for x in range(21)]

    def set_unonwed(self, card_number : int) -> None:
        self.cards[card_number] = -1
        self.unowned_cards += 1
    
    def set_owned(self, card_number : int) -> None:
        self.cards[card_number] = 1
        self.owned_cards += 1

    def get_card_state(self, card_number: int) -> int:
        return self.cards[card_number]

    def analyze_hand(self, CARDS_PER_HAND : int, sidon_sum : int) -> list[int]:
        changes = []

        # See if all owned or unowned cards are accounted for
        if owned_cards == CARDS_PER_HAND:
            changes += [-1]
            for i in range(21):
                if cards[i] != 1:
                    self.set_unowned(i)
        elif unowned_cards == 21 - CARDS_PER_HAND:
            changes += [1]
            for i in range(21):
                if cards[i] != -1:
                    self.set_owned(i)
                    changes += [i]        
        else:
            for i in range(21):
                if cards[i] == sidon_sum:
                    self.set_owned(i)
                    changes += [i]
        return changes
    
    def output(self) -> list[str]:
        def to_printable(x : int) -> str:
            if x == -1:
                return "-"
            if x == 0:
                return " "
            if x == 1:
                return "X"
            return "*"
        return [self.name[0]] + [to_printable(x) for x in cards]
