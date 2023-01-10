class Sheet():

    def __init__(self, p):
        global notecard
        global players
        players = p
        notecard = [['Col. Mustard\t', 'Prof. Plum\t','Mr. Green\t', 'Mrs. Peacock\t', 'Miss Scarlet\t', 'Mrs. White\t', 
                   'Knife\t\t', 'Candlestick\t', 'Revolver\t', 'Rope\t\t', 'Lead Pipe\t', 'Wrench\t', 
                   'Hall\t\t', 'Lounge\t', 'Dining Room\t', 'Kitchen\t', 'Ballroom\t', 'Conservatory\t', 'Billiard Room\t', 'Library\t', 'Study\t\t']] + [[' '] * 21 for _ in range(len(players))]
        print('Enter the number of your cards and the communal cards, separated by spaces: ')
        for i in range(1, 22):
            print('\n\t', i, ' - ', notecard[0][i - 1])
        user_cards = input('Enter your cards: ').split(' ')
        
        print(self)
    
    def __str__(self):
        s = '=' * 18 + '=' * len(notecard) * 3
        for j in range(21):
            s += '\n| '
            for i in range(len(notecard)):
                s += notecard[i][j] + ' | '
            if j == 5 or j == 11:
                s += '\n' + '=' * 18 + '=' * len(notecard) * 3
        s += '\n' + '=' * 18 + '=' * len(notecard) * 3
        return s

    def move(self):
        print('For each prompt, please enter the number that corresponds to the suggestion\n')
        print('Who is being suggested?')
        for i in range(1, 7):
            print('\n\t', i, ' - ', notecard[0][i - 1])
        p = (int(input('Enter a number: ')) - 1)

        print('\n\nWhat weapon is being suggested?')
        for i in range(1, 7):
            print('\n\t', i, ' - ', notecard[0][i + 5])
        w = (int(input('Enter a number: ')) + 5)

        print('\n\nWhat room is being suggested?')
        for i in range(1, 10):
            print('\n\t', i, ' - ', notecard[0][i + 11])
        r = (int(input('Enter a number: ')) + 11)

        print('\n\nWho made the move?')
        for i in range(1, len(players) + 1):
            print('\n\t', i, ' - ', players[i - 1])
        s = (int(input('Enter a number: ')) - 1)

        print('\n\nWho disproved the move?')
        for i in range(1, len(players) + 1):
            print('\n\t', i, ' - ', players[i - 1])
        print('\n\t', len(players) + 1, ' - No one')
        d = (int(input('Enter a number: ')) - 1)

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
        else:
            players_skipped = [x for x in list(range(len(players))) if x != s]
        for i in players_skipped:
            print(notecard[i+1][p])
            notecard[i+1][p] = '-'
            notecard[i+1][w] = '-'
            notecard[i+1][r] = '-'
        


def test_sheet():
    s = Sheet(['Chris', 'Winnie', 'Harrison'])
    print(s)
    s.move()
    print(s)

if __name__ == '__main__':
    test_sheet()

