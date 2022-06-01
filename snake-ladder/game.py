
import time
from dice import Dice
from board import Board
class Game:

    def __init__(self, players=[]):
        self.players = players
        self.game_dice = Dice()
        self.board = Board()

    def start_play(self):
        while True:
            for p in self.players:
                self.board.display_board()
                dice_val = self.game_dice.play_dice()
                next_pos  = self.board.get_pos_in_no(p.pos) + dice_val
                if not self.board.is_valid_pos(next_pos):
                    continue
                print("{} next move is {} and new position is {}".format(p.name, dice_val, next_pos))
                p.update_pos(self.board.get_pos_in_x_y(next_pos))
                if self.board.has_player_won(p):
                    return ("{} has won".format(p.name))
                time.sleep(2)
