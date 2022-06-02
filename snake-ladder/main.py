from game import Game
from player import Player
import sys

if __name__ == '__main__':
    while True:
        no_of_snakes = int(input("Enter no. of snakes: "))
        no_of_ladders = int(input("Enter no. of ladders: "))
        snake_n_ladders = {}
        while no_of_snakes > 0:
            st = int(input("Enter start. of snake: "))
            if st in snake_n_ladders:
                print("There is already a snake/ladder in the this pos")
                continue
            else:
                en = int(input("Enter end. of snake: "))
                snake_n_ladders[st] = en
            no_of_snakes -= 1

        while no_of_ladders > 0:
            st = int(input("Enter start. of ladder: "))
            if st in snake_n_ladders:
                print("There is already a snake/ladder in the this pos")
                continue
            else:
                en = int(input("Enter end. of ladder: "))
                snake_n_ladders[st] = en
            no_of_ladders -= 1


        no_of_players = int(input("Enter no. of players: "))
        players = []
        while no_of_players > 0:
            name = input("Enter name of player: ")
            players.append(Player(name))
            no_of_players -= 1

        game = Game(players, snake_n_ladders)
        print(game.start_play())
        sys.exit()
