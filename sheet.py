class Sheet():

    def __init__(self, num_players):
        global notecard
        notecard = [['Colonel Mustard', 'Professor Plum','Mr. Green', 'Mrs. Peacock', 'Miss Scarlet', 'Mrs. White', 
                   'Knife', 'Candlestick', 'Revolver', 'Rope', 'Lead Pipe', 'Wrench', 
                   'Hall', 'Lounge', 'Dining Room', 'Kitchen', 'Ballroom', 'Conservatory', 'Billiard Room', 'Library', 'Study']] + [] * num_players
    
    def __str__(self):
        s = ' - ' * len(notecard)
        for j in range(21):
            s += '\n | '
            for i in range(len(notecard)):
                s += notecard[i][j] + ' | '
        s += '\n' + ' - ' * len(notecard)
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
        print('\nThis move has been logged')
        print(notecard[0][person], notecard[0][weapon], notecard[0][room])

def test_sheet():
    s = Sheet(3)
    s.move()

if __name__ == '__main__':
    test_sheet()

