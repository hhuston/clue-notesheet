from sheet import NoteSheet

class ClueGame():
    
    def play_game(self):
        game_sheet = NoteSheet(self.get_players())
        print('\n')
        while not game_sheet.answer_known():
            print(game_sheet)
            s, p, w, r, d = game_sheet.get_move_input()
            game_sheet.move(s, p, w, r, d)
        person, weapon, room = game_sheet.answer()
        print('It was', person, 'with the', weapon, 'in the', room)

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
    
if __name__ == '__main__':
    game = ClueGame()
    game.play_game()
    
