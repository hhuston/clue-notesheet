class NoteSheet():

    def __init__(self, p):
        global notecard
        global players
        global possibilities
        global answers
        players = p
        possibilities = [[0] * 24 for _ in range(len(players) + 1)]
        notecard = [['Col. Mustard\t', 'Prof. Plum\t','Mr. Green\t', 'Mrs. Peacock\t', 'Miss Scarlet\t', 'Mrs. White\t', 
                   'Knife\t\t', 'Candlestick\t', 'Revolver\t', 'Rope\t\t', 'Lead Pipe\t', 'Wrench\t', 
                   'Hall\t\t', 'Lounge\t', 'Dining Room\t', 'Kitchen\t', 'Ballroom\t', 'Conservatory\t', 'Billiard Room\t', 'Library\t', 'Study\t\t']] + [[' '] * 21 for _ in range(len(players))]
        print('Enter the number of your cards and the communal cards, separated by spaces: ')
        answers = [len(players)] * 21 + [''] * 3
        for i in range(1, 22):
            print('\t', i, ' - ', notecard[0][i - 1])
        user_cards = input('Enter your cards: ').split(' ')
        user_cards = [int(x) - 1 for x in user_cards]
        for card in range(21):
            if card in user_cards:
                notecard[len(notecard) - 1][card] = 'X'
                for player in range(1, len(notecard) - 1):
                    notecard[player][card] = '-'
                    possibilities[player][23] += 1
            else:
                notecard[len(notecard) - 1][card] = '-'
                self.update_answers(card)

    def get_move_input(self):
        prompt = 'Enter a number: '
        print('For each prompt, please enter the number that corresponds to the suggestion')
        
        print('\nWho made the suggestion?')
        for i in range(1, len(players) + 1):
            print('\t', i, ' - ', players[i - 1])
        suggestor = (int(input(prompt)) - 1)
        
        print('\nWhat person is being suggested?')
        for i in range(1, 7):
            print('\t', i, ' - ', notecard[0][i - 1])
        person = (int(input(prompt)) - 1)

        print('\nWhat weapon is being suggested?')
        for i in range(1, 7):
            print('\t', i, ' - ', notecard[0][i + 5])
        weapon = (int(input(prompt)) + 5)

        print('\nWhat room is being suggested?')
        for i in range(1, 10):
            print('\t', i, ' - ', notecard[0][i + 11])
        room = (int(input(prompt)) + 11)

        print('\nWho disproved the suggestion?')
        for i in range(1, len(players) + 1):
            print('\t', i, ' - ', players[i - 1])
        print('\t', len(players) + 1, ' -  No one')
        disprover = (int(input(prompt)) - 1)
        return suggestor, person, weapon, room, disprover

    def move(self, s, p, w, r, d):
        global players_skipped
        players_skipped = []
        if d != len(players):
            i = s + 1
            while True:
                if i == len(players):
                    i = 0
                if i == d:
                    break
                players_skipped += [i]
                i += 1
            s += 1
            d += 1
            self.record_player_disprove(s, p, w, r, d)
        else:
            players_skipped = [x for x in list(range(len(players))) if x != s]
        self.fill_skipped_players(p, w, r)
        for player in range(1, len(players)):
            self.update_possibile_cards(player)
        for player in range(len(players) - 2, 0, -1):
            self.update_possibile_cards(player)

    def fill_skipped_players(self, p, w, r):
        global players_skipped
        global answers
        for player in players_skipped:
            for card in [p, w, r]:
                if notecard[player + 1][card] != '-':
                    notecard[player + 1][card] = '-'
                    possibilities[player + 1][23] += 1
                    self.update_answers(card)

    def record_player_disprove(self, s, p, w, r, d):
        self.only_possibility(p, w, r, d)
        if s != len(players) and d != len(players):
            possibilities[d][21] = possibilities[d][21] + 1 if possibilities[d][21] != 0 else 3
            for j in [p, w, r]:
                if notecard[d][j] != '-':
                    notecard[d][j] = '*' if notecard[d][j] == ' ' else 'X'
                    possibilities[d][j] += possibilities[d][21]
        elif d != len(players):
            print('\nWhat card did', players[d - 1], 'show you?\n\t1 - ', notecard[0][p])
            print('\t2 - ', notecard[0][w], '\n\t3 - ', notecard[0][r])
            shown_card = int(input('Enter a number: '))
            match shown_card:
                case 1:
                    shown_card = p
                case 2:
                    shown_card = w
                case 3:
                    shown_card = r
            self.set_card_owner(d, shown_card)

    def only_possibility(self, p, w, r, d):
        if notecard[d][p] == '-' and notecard[d][w] == '-':
            self.set_card_owner(d, r)
        elif notecard[d][p] == '-' and notecard[d][r] == '-':
            self.set_card_owner(d, w)
        elif notecard[d][w] == '-' and notecard[d][r] == '-':
            self.set_card_owner(d, p)
        
    def set_card_owner(self, owner, card):
        notecard[owner][card] = 'X'
        possibilities[owner][22] += 1
        for player in range(1, len(notecard) - 1):
            if player != owner and notecard[player][card] != '-':
                notecard[player][card] = '-'
                possibilities[player][23] += 1
                self.update_answers(card)

    # Check the logic in these
    def update_possibile_cards(self, player):
        if possibilities[player][22] == 3 and possibilities[player][23] != 18:
            self.all_owned_found(player)
        elif possibilities[player][23] == 18 and possibilities[player][22] != 3:
            self.all_unowned_found(player)
        t3, t4, t5 = self.get_possibilities(player)
        for j in [3, 4, 5, 4, 3]:
            if j == 3 and len(t3) == 1 and notecard[player][t3[0]] != 'X':
                self.one_in_tracker(player, t3, t4, t5)
            elif j == 4 and len(t4) == 1 and notecard[player][t4[0]] != 'X':
                self.one_in_tracker(player, t4, t5, t3)
            elif j == 5 and len(t5) == 1 and notecard[player][t5[0]] != 'X':
                self.one_in_tracker(player, t5, t3, t4)
        self.nine_possibilities(player, t3 + t4 + t5)

    def all_owned_found(self, player):
        for card in range(21):
            if notecard[player][card] != 'X' and notecard[player][card] != '-':
                notecard[player][card] = '-'
                self.update_answers(card)
    
    def all_unowned_found(self, player):
        for card in range(21):
            if notecard[player][card] == ' ' or notecard[player][card] == '*':
                self.set_card_owner(player, card)

    def get_possibilities(self, player):
        tracker_3, tracker_4, tracker_5 = [], [], []
        for j in range(21):
            if possibilities[player][j] in [3, 7, 8, 12] and notecard[player][j] != '-':
                tracker_3 += [j]
            if possibilities[player][j] in [4, 7, 9, 12] and notecard[player][j] != '-':
                tracker_4 += [j]
            if possibilities[player][j] in [5, 8, 9, 12] and notecard[player][j] != '-':
                tracker_5 += [j]
        return tracker_3, tracker_4, tracker_5

    def one_in_tracker(self, i, a, b, c):
        self.set_card_owner(i, a[0])
        if a[0] in b:
            b.remove(a[0])
        if a[0] in c:
            c.remove(a[0])    
    
    def nine_possibilities(self, player, all_trackers):
        if len(all_trackers) == 9:
            for card in range(21):
                if card not in all_trackers and notecard[player][card] == ' ':
                    notecard[player][card] = '-'
                    possibilities[player][23] += 1
                    self.update_answers(card)
    
    def update_answers(self, card):
        global answers
        answers[card] -= 1
        if answers[card] == 0 and 0 <= card <= 5:
            answers[21] = notecard[0][card].strip()
        elif answers[card] == 0 and 6 <= card <= 11:
            answers[22] = notecard[0][card].strip()
        elif answers[card] == 0 and 12 <= card <= 20:
            answers[23] = notecard[0][card].strip()


    def answer_known(self):
        return answers[21] != '' and answers[22] != '' and answers[23] != ''

    def answer(self):
        return answers[21], answers[22], answers[23]

    def __str__(self):
        s = '\n\n\t\t | ' + ' | '.join([name[0] for name in players]) + ' |\n'
        s += '=' * 18 + '=' * len(players) * 4
        for j in range(21):
            s += '\n| '
            for i in range(len(notecard)):
                s += notecard[i][j] + ' | '
            if j == 5 or j == 11:
                s += '\n' + '=' * 18 + '=' * len(players) * 4
        s += '\n' + '=' * 18 + '=' * len(players) * 4
        return s