# from collections import defaultdict

class Board:
    """docstring for ."""

    def __init__(self, snake_n_ladders={}, n=10, m=10):
        self.snake_n_ladders = snake_n_ladders
        self.n = n
        self.m = m
        self.position_h = {}

        c = 1
        self.board_arr = [[0 for _ in range(self.n)] for _ in range(self.m)]
        for i in range(self.m):
            if i%2 == 0:
                for j in range(self.n):
                        self.board_arr[i][j] = c
                        self.position_h[c] = (i, j)
                        self.position_h[(i, j)] = c
                        c += 1
            else:
                for j in range(self.n-1, -1, -1):
                        self.board_arr[i][j] = c
                        self.position_h[c] = (i, j)
                        self.position_h[(i, j)] = c
                        c += 1

    def assign_snake_n_ladders(self, snake_n_ladders):
        self.snake_n_ladders = snake_n_ladders


    def get_final_pos(self, pos, seen=set()):
        if pos not in self.snake_n_ladders or pos in seen:
            return pos
        seen.add(pos)
        return self.get_final_pos(self.snake_n_ladders[pos], seen)

    def has_player_won(self, player):
        return player.pos == self.get_pos_in_x_y((self.n * self.m))
        # return True

    def get_pos_in_x_y(self, pos):
        return self.position_h[pos]

    def get_pos_in_no(self, pos):
        return self.position_h[pos]

    def is_valid_pos(self, final_pos):
        if final_pos not in self.position_h:
            return False
        x, y = self.get_pos_in_x_y(final_pos)
        return 0 <= x < self.m and 0 <= y < self.n

    def display_board(self):
        for i in range(self.m -1, -1, -1):
            for j in range(self.n):
                print(self.board_arr[i][j], end = '\t')
            print()
