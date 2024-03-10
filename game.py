from board import Ship,Board #important for the project

## Uncomment the following lines when you are ready to do input/output tests!
## Make sure to uncomment when submitting to Codio.
import sys
def input( prompt=None ):
   if prompt != None:
       print( prompt, end="" )
   aaa_str = sys.stdin.readline()
   aaa_str = aaa_str.rstrip( "\n" )
   print( aaa_str )
   return aaa_str


class Player(object):
    """
        The Player class represents a single player of battleship.
    """
    def __init__(self, name, board, ship_list):
        """
            Creates a Player object.
        """

        self.name = name
        self.board = board
        self.ship_list = [ship_list]
        self.guesses = []

    def validate_guess(self, guess):
        """
            This method takes a guess tuple and checks if it is valid.
        """

        row, col = guess

        # Raise an error if the guess has already been made
        if guess in self.guesses:

            raise RuntimeError("This guess has already been made!")

        # If the coordinates are not on the board raise an error
        if not (0 <= row < self.board.size and 0 <= col < self.board.size):

            raise RuntimeError("Guess is not a valid location!")

    def get_player_guess(self):
        """
            This method will read a guess from the user using a prompt
        """

        while True:
            try:
                # Get a guess from the player (Row, Col)
                guess_str = input("Enter your guess: ")
                guess = tuple(map(int, guess_str.split(',')))

                # Check to see if the guess is valid
                # If the guess is valid add it to the guesses list
                self.validate_guess(guess)
                self.guesses.append(guess)
                return guess

            # Raise an error if anything fails during this def
            except RuntimeError as e:
                print(e)

    def set_all_ships(self): # Fix
        '''
            Thies function will place ships for the player
        '''

        # For each ship size [(5, 4, 3, 3, 2)] in the list
        for size in self.ship_list:
            for i in size:

                while True:

                    # Prompt the user for coordinates and orientation of a ship placement
                    coord_str = input(f"Enter the coordinates of the ship of size {i}: ")
                    orientation = input(f"Enter the orientation of the ship of size {i}: ")
                    ship = Ship(i, tuple(map(int, coord_str.split(','))), orientation)

                    try:
                        # Check to see if the coordinates are a valid placement
                        # If they are place the ship onto the board
                        self.board.validate_ship_coordinates(ship)
                        self.board.place_ship(ship)
                        break

                    # If the validate_ship_coordinates fails raise an error
                    except RuntimeError as e:
                        print(e)
                        continue


class BattleshipGame(object):
    """
        This class is responsible for running the game, keeping
        track of turns, and checking if a player has won.
    """

    def __init__(self, player1, player2):
        """
            Initialize player1 and player2
        """

        self.player1 = player1
        self.player2 = player2

    def check_game_over(self):
        """
            Checks if the game has ended, I.e. all of the
            opponents ships have been sunk.
        """

        # If all the ships in the ship list return true from the is_sunk def
        # in player1's list, return player2's name as winner
        if all(ship.is_sunk for ship in self.player1.board.ships):
            return self.player2.name

        # If all the ships in the ship list return true from the is_sunk def
        # in player2's list, return player1's name as winner
        elif all(ship.is_sunk for ship in self.player2.board.ships):
            return self.player1.name

        # If neither, return an empty string
        else:
            return ''

    def display(self):
        """
            Displays the current state of the game
        """

        # Print each players name and current board state
        print(f"{self.player1.name}'s board:")
        print(self.player1.board)
        print(f"{self.player2.name}'s board:")
        print(self.player2.board)

    def play(self):
        """
            This method will run the entire game until one of the players
            has won.
        """

        while True:

            # Use hasattr to allow this segment of code to only
            # run once per game
            if not hasattr(self, 'ships_placed'):
                self.ships_placed = True

                # Have each player place their ships
                self.player1.set_all_ships()
                self.player2.set_all_ships()


            # Display the current state of each player's board
            self.display()

            # Player 1's Turn for guesses
            print(f"{self.player1.name}'s turn.")
            guess1 = self.player1.get_player_guess()
            self.player2.board.apply_guess(guess1)
            winner = self.check_game_over()
            if winner != '':
                print(f"{winner} wins!")
                break

            # Player 2's Turn for guesses
            print(f"{self.player2.name}'s turn.")
            guess2 = self.player2.get_player_guess()
            self.player1.board.apply_guess(guess2)
            winner = self.check_game_over()
            if winner != '':
                print(f"{winner} wins!")
                break

            # Ask if the user would like to keep playing after each turn
            continue_play = input("Continue playing?: ")
            if continue_play == 'q':
                break
