from game import Game
from player import Player
import sys

if __name__ == '__main__':
    while True:
        no_of_players = int(input("Enter no. of players: "))
        players = []
        while no_of_players > 0:
            name = input("Enter name of player: ")
            players.append(Player(name))
            no_of_players -= 1

        game = Game(players)
        print(game.start_play())
        sys.exit()
