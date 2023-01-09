class Sheet():

    def __init__(self, num_players):
        global notecard
        notecard = [['Col. Mustard\t', 'Prof. Plum\t','Mr. Green\t', 'Mrs. Peacock\t', 'Miss Scarlet\t', 'Mrs. White\t', 
                   'Knife\t\t', 'Candlestick\t', 'Revolver\t', 'Rope\t\t', 'Lead Pipe\t', 'Wrench\t', 
                   'Hall\t\t', 'Lounge\t', 'Dining Room\t', 'Kitchen\t', 'Ballroom\t', 'Conservatory\t', 'Billiard Room\t', 'Library\t', 'Study\t\t']] + ([[' '] * 21] * num_players)
    
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
        print('Who is being suggested?', '\n\t', 1, ' - ', notecard[0][0], '\n\t', 2, ' - ', notecard[0][1], '\n\t', 3, ' - ', notecard[0][2],
            '\n\t', 4, ' - ', notecard[0][3], '\n\t', 5, ' - ', notecard[0][4], '\n\t', 6, ' - ', notecard[0][5])
        person = (int(input('Enter a number: ')) - 1)

        print('\n\nWhat weapon is being suggested?', '\n\t', 1, ' - ', notecard[0][6], '\n\t', 2, ' - ', notecard[0][7], '\n\t', 3, ' - ', notecard[0][8],
            '\n\t', 4, ' - ', notecard[0][9], '\n\t', 5, ' - ', notecard[0][10], '\n\t', 6, ' - ', notecard[0][11])
        weapon = (int(input('Enter a number: ')) + 5)

        print('\n\nWhat room is being suggested?', '\n\t', 1, ' - ', notecard[0][12], '\n\t', 2, ' - ', notecard[0][13], '\n\t', 3, ' - ', notecard[0][14],
            '\n\t', 4, ' - ', notecard[0][15], '\n\t', 5, ' - ', notecard[0][16], '\n\t', 6, ' - ', notecard[0][17], '\n\t', 7, ' - ', notecard[0][18],
            '\n\t', 8, ' - ', notecard[0][19], '\n\t', 9, ' - ', notecard[0][20])
        room = (int(input('Enter a number: ')) + 11)
        

def test_sheet():
    s = Sheet(3)
    # s.move()
    print(s)

if __name__ == '__main__':
    test_sheet()

