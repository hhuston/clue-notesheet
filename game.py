import sheet

class ClueGame():
    
    def play_game(self):
        game_sheet = sheet.NoteSheet(self.get_players())
        print('\n')
        game_sheet.move(game_sheet.get_move_input())

    def get_players(self):
        while True:
            names = input('Enter each player\'s name in turn order with your name at the end, separated by spaces:\n')
            names = names.strip().split(' ')
            if len(names) <= 1:
                print('Too few players')
            elif len(names) >= 7:
                print('Too many players')
            else:
                return names
    
    
