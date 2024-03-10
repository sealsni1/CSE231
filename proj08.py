'''
CSE231 - Fall 2023
Project 08: Battleship Game

Description:
This program implements the game of Battleship. It consists of four
classes: Ship, Board, Player, and BattleshipGame.
Players place their ships on the board in the first part of the game
and take turns making guesses in the second part.
The game ends when one player sinks all the opponent's ships.

Files:
board.py: Contains the Ship and Board Classes
game.py: Contains the Player and BattleshipGame Classes
proj08.py: Main program that runs the game

'''

from board import Ship, Board #important for the project
from game import Player, BattleshipGame #important for the project





def main():

    # Assign the board size and ship sizes list
    board_size = 5
    ship_list = [5, 4, 3, 3, 2]

    # Create a board for each player
    board1 = Board(board_size)
    board2 = Board(board_size)

    # Assign each player in the game
    player1 = Player("Player 1", board1, ship_list)
    player2 = Player("Player 2", board2, ship_list)

    # Assign game to the BattleshipGame class using each player
    # and then play the game using the play() method from the class
    game = BattleshipGame(player1, player2)
    game.play()

if __name__ == "__main__":
    main()