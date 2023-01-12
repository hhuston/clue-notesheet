class Sheet():

    def __init__(self, p):
        global notecard
        global players
        global trackers
        players = p
        trackers = [[0] * 24 for _ in range(len(players) + 1)]
        notecard = [['Col. Mustard\t', 'Prof. Plum\t','Mr. Green\t', 'Mrs. Peacock\t', 'Miss Scarlet\t', 'Mrs. White\t', 
                   'Knife\t\t', 'Candlestick\t', 'Revolver\t', 'Rope\t\t', 'Lead Pipe\t', 'Wrench\t', 
                   'Hall\t\t', 'Lounge\t', 'Dining Room\t', 'Kitchen\t', 'Ballroom\t', 'Conservatory\t', 'Billiard Room\t', 'Library\t', 'Study\t\t']] + [[' '] * 21 for _ in range(len(players))]
        print('Enter the number of your cards and the communal cards, separated by spaces: ')
        for i in range(1, 22):
            print('\n\t', i, ' - ', notecard[0][i - 1])
        user_cards = input('Enter your cards: ').split(' ')
        user_cards = [int(x) - 1 for x in user_cards]
        for i in range(21):
            if i in user_cards:
                notecard[len(notecard) - 1][i] = 'X'
                for j in range(1, len(notecard) - 1):
                    notecard[j][i] = '-'
                    trackers[j][23] += 1
            else:
                notecard[len(notecard) - 1][i] = '-'

    def set_card_owner(self, person, card):
        notecard[person][card] = 'X'
        trackers[person][22] += 1
        for i in range(1, len(notecard) - 1):
            if i != person:
                notecard[i][card] = '-'
                trackers[i][23] += 1

    def get_move_input(self):
        prompt = 'Enter a number: '
        print('For each prompt, please enter the number that corresponds to the suggestion\n')
        
        print('Who made the suggestion?')
        for i in range(1, len(players) + 1):
            print('\n\t', i, ' - ', players[i - 1])
        suggestor = (int(input(prompt)) - 1)
        
        print('\n\nWhat person is being suggested?')
        for i in range(1, 7):
            print('\n\t', i, ' - ', notecard[0][i - 1])
        person = (int(input(prompt)) - 1)

        print('\n\nWhat weapon is being suggested?')
        for i in range(1, 7):
            print('\n\t', i, ' - ', notecard[0][i + 5])
        weapon = (int(input(prompt)) + 5)

        print('\n\nWhat room is being suggested?')
        for i in range(1, 10):
            print('\n\t', i, ' - ', notecard[0][i + 11])
        room = (int(input(prompt)) + 11)

        print('\n\nWho disproved the suggestion?')
        for i in range(1, len(players) + 1):
            print('\n\t', i, ' - ', players[i - 1])
        print('\n\t', len(players) + 1, ' -  No one')
        disprover = (int(input(prompt)) - 1)
        return suggestor, person, weapon, room, disprover

    def move(self, s, p, w, r, d):
        global players_skipped
        players_skipped = []
        if d != len(players):
            self.record_player_disprove(s, p, w, r, d)
        else:
            players_skipped = [x for x in list(range(len(players))) if x != s]
        for i in players_skipped:
            print(notecard[i+1][p])
            for j in [p, w, r]:
                if notecard[i+1][j] != '-':
                    notecard[i+1][j]= '-'
                    trackers[i+1][23] += 1

    def record_player_disprove(self, s, p, w, r, d):
        global players_skipped
        i = s + 1
        while True:
            if i == len(players):
                i = 0
            if i == d:
                break
            players_skipped += [i]
            i += 1
        d += 1
        if notecard[d][p] == '-' and notecard[d][w] == '-':
            self.set_card_owner(d, r)
        elif notecard[d][p] == '-' and notecard[d][r] == '-':
            self.set_card_owner(d, w)
        elif notecard[d][w] == '-' and notecard[d][r] == '-':
            self.set_card_owner(d, p)
        elif s != len(players) - 1:
            trackers[d][21] = trackers[d][21] + 1 if trackers[d][21] != 0 else 3
            count = trackers[d][21]
            for j in [p, w, r]:
                if notecard[d][j] != '-':
                    notecard[d][j] = '*'
                    trackers[d][j] += count
        else:
            print('\n\nWhat card did', players[d - 1], 'show you?\n\t1 - ', notecard[0][p])
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

    def check_possibile_cards(self, player):
        # for i in range(1, len(players)):
        if trackers[player][22] == 3 and trackers[player][23] != 18:
            notecard[player] = list(map(lambda x: '-' if x == ' ' else 'X', notecard[player]))
            return
        if trackers[player][23] == 18 and trackers[player][22] != 3:
            for j in range(21):
                if notecard[player][j] == ' ':
                    self.set_card_owner(player, j)
            return
        t3, t4, t5 = self.get_possible_cards(player)
        for j in [3, 4, 5, 4, 3]:
            if j == 3 and len(t3) == 1:
                self.one_in_tracker(player, t3, t4, t5)
            elif j == 4 and len(t4) == 1:
                self.one_in_tracker(player, t4, t5, t3)
            elif j == 5 and len(t5) == 1:
                self.one_in_tracker(player, t5, t3, t4)
        all_trackers = t3 + t4 + t5
        if len(all_trackers) == 9:
            for j in range(21):
                if j not in all_trackers:
                    notecard[player][j] = '-'
                    trackers[player][23] += 1

    def get_possible_cards(self, player):
        tracker_3, tracker_4, tracker_5 = [], [], []
        for j in range(21):
            if trackers[player][j] in [3, 7, 8, 12] and notecard[player][j] != '-':
                tracker_3 += [j]
            if trackers[player][j] in [4, 7, 9, 12] and notecard[player][j] != '-':
                tracker_4 += [j]
            if trackers[player][j] in [5, 8, 9, 12] and notecard[player][j] != '-':
                tracker_5 += [j]
        return tracker_3, tracker_4, tracker_5

    def one_in_tracker(self, i, a, b, c):
        self.set_card_owner(i, a[0])
        if a[0] in b:
            b.remove(a[0])
        if a[0] in c:
            c.remove(a[0])

    def __str__(self):
        s = '\n\n\t\t | ' + ' | '.join([name[0] for name in players]) + ' |\n'
        s += '=' * 18 + '=' * len(notecard) * 3
        for j in range(21):
            s += '\n| '
            for i in range(len(notecard)):
                s += notecard[i][j] + ' | '
            if j == 5 or j == 11:
                s += '\n' + '=' * 18 + '=' * len(notecard) * 3
        s += '\n' + '=' * 18 + '=' * len(notecard) * 3
        return s