class Sheet():

    def __init__(self, p):
        global notecard
        global players
        global players_count
        global trackers
        players = p
        players_count = [[0] * len(players)]
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

    def move(self):
        prompt = 'Enter a number: '
        print('For each prompt, please enter the number that corresponds to the suggestion\n')
        
        print('\n\nWho made the suggestion?')
        for i in range(1, len(players) + 1):
            print('\n\t', i, ' - ', players[i - 1])
        s = (int(input(prompt)) - 1)
        
        print('Who is being suggested?')
        for i in range(1, 7):
            print('\n\t', i, ' - ', notecard[0][i - 1])
        p = (int(input(prompt)) - 1)

        print('\n\nWhat weapon is being suggested?')
        for i in range(1, 7):
            print('\n\t', i, ' - ', notecard[0][i + 5])
        w = (int(input(prompt)) + 5)

        print('\n\nWhat room is being suggested?')
        for i in range(1, 10):
            print('\n\t', i, ' - ', notecard[0][i + 11])
        r = (int(input(prompt)) + 11)

        print('\n\nWho disproved the suggestion?')
        for i in range(1, len(players) + 1):
            print('\n\t', i, ' - ', players[i - 1])
        print('\n\t', len(players) + 1, ' -  No one')
        d = (int(input(prompt)) - 1)

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
            d += 1
            if notecard[d][p] == '-' and notecard[d][w] == '-':
                notecard[d][r] = 'X'
                trackers[d][22] += 1
                for i in range(1, len(notecard) - 1):
                    if i != d:
                        notecard[i][r] = '-'
                        trackers[i][23] += 1
            elif notecard[d][p] == '-' and notecard[d][r] == '-':
                notecard[d][w] = 'X'
                trackers[d][22] += 1
                for i in range(1, len(notecard) - 1):
                    if i != d:
                        notecard[i][w] = '-'
                        trackers[i][23] += 1
            elif notecard[d][w] == '-' and notecard[d][r] == '-':
                notecard[d][p] = 'X'
                trackers[d][22] += 1
                for i in range(1, len(notecard) - 1):
                    if i != d:
                        notecard[i][p] = '-'
                        trackers[i][23] += 1
            else:
                trackers[d][21] = trackers[d][21] + 1 if trackers[d][21] != 0 else 3
                count = trackers[d][21]

                if notecard[d][p] != '-':
                    notecard[d][p] = '*'
                    trackers[d][p] += count
                if notecard[d][w] != '-':
                    notecard[d][w] = '*'
                    trackers[d][w] += count
                if notecard[d][r] != '-':
                    notecard[d][r] = '*'
                    trackers[d][r] += count

        else:
            players_skipped = [x for x in list(range(len(players))) if x != s]
        for i in players_skipped:
            print(notecard[i+1][p])
            if notecard[i+1][p] != '-':
                notecard[i+1][p]= '-'
                trackers[i+1][23] += 1
            if notecard[i+1][w] != '-':
                notecard[i+1][w] = '-'
                trackers[i+1][23] += 1
            if notecard[i+1][r] != '-':
                notecard[i+1][r] = '-'
                trackers[i+1][23] += 1

        for i in range(1, len(players)):
            if trackers[i][22] == 3 and trackers[i][23] != 18:
                notecard[i] = list(map(lambda x: '-' if x == ' ' else 'X', notecard[i]))
            elif trackers[i][23] == 18 and trackers[i][22] != 3:
                for j in range(21):
                    if notecard[i][j] == ' ':
                        notecard[i][j] = 'X'
                        trackers[i][22] += 1
                        for k in range(1, len(notecard) - 1):
                            if k != i:
                                notecard[k][j] = '-'
                                trackers[k][23] += 1
            else:
                tracker_3 = []
                tracker_4 = []
                tracker_5 = []
                for j in range(21):
                    if trackers[i][j] in [3, 7, 8, 12] and notecard[i][j] != '-':
                        tracker_3 += [j]
                    if trackers[i][j] in [4, 7, 9, 12] and notecard[i][j] != '-':
                        tracker_4 += [j]
                    if trackers[i][j] in [5, 8, 9, 12] and notecard[i][j] != '-':
                        tracker_5 += [j]
                for j in [3, 4, 5, 4, 3]:
                    if j == 3 and len(tracker_3) == 1:
                        notecard[i][tracker_3[0]] = 'X'
                        trackers[i][22] += 1
                        for k in range(1, len(notecard) - 1):
                            if k != i:
                                notecard[k][j] = '-'
                                trackers[k][23] += 1
                        if tracker_3[0] in tracker_4:
                            tracker_4.remove(tracker_3[0])
                        if tracker_3[0] in tracker_5:
                            tracker_5.remove(tracker_3[0])
                    elif j == 4 and len(tracker_4) == 1:
                        notecard[i][tracker_4[0]] = 'X'
                        trackers[i][22] += 1
                        for k in range(1, len(notecard) - 1):
                            if k != i:
                                notecard[k][j] = '-'
                                trackers[k][23] += 1
                        if tracker_4[0] in tracker_3:
                            tracker_3.remove(tracker_4[0])
                        if tracker_4[0] in tracker_5:
                            tracker_5.remove(tracker_4[0])
                    elif j == 5 and len(tracker_5) == 1:
                        notecard[i][tracker_5[0]] = 'X'
                        trackers[i][22] += 1
                        for k in range(1, len(notecard) - 1):
                            if k != i:
                                notecard[k][j] = '-'
                                trackers[k][23] += 1
                        if tracker_5[0] in tracker_4:
                            tracker_4.remove(tracker_5[0])
                        if tracker_5[0] in tracker_3:
                            tracker_3.remove(tracker_5[0])
                all_tracker = tracker_3 + tracker_4 + tracker_5
                if len(all_tracker) == 9:
                    for j in range(21):
                        if j not in all_tracker:
                            notecard[i][j] = '-'
                            trackers[i][23] += 1


def test_sheet():
    s = Sheet(['Chris', 'Winnie', 'Harrison'])
    print(s)
    s.move()
    print(s)

if __name__ == '__main__':
    test_sheet()

