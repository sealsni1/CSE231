import sys
import NMM  # This is necessary for the project

#########################################################################################
# Project 07
# Nine Men's Morris
#
# Prompt the user for a command to place a piece on the board class created in NMM.py.
#
# Once each player has placed 9 pieces (18 total) in a back, and fourth continuation, the
# second phase will begin.
#
# while prompting the user for a point, the program will be checking if the point is on
# the board, not occupied, and if that piece will create a mill.
#
# If the piece does create a mill, it will then prompt the user to remove one of their
# opponents pieces from the board (this piece cannot be in a mill unless no other pieces are
# available).
#
# Once all 18 pieces are placed on the board, the program will then prompt the user to move
# their pieces to points adjacent to the piece they choose to move while checking if the
# origin and destination of the move are valid options.
#
# If the move is valid, and it creates a mill, the player is then allowed to remove one
# of their opponents pieces.
#
# While Phase two is in action the program will be checking if the users opponent has less
# than two pieces remaining on the board, and if so the program will execute a statement to
# display a BANNER that congratulates the player on winning the game
#
#########################################################################################

BANNER = """
    __      _(_)_ __  _ __   ___ _ __| | |
    \ \ /\ / / | '_ \| '_ \ / _ \ '__| | |
     \ V  V /| | | | | | | |  __/ |  |_|_|
      \_/\_/ |_|_| |_|_| |_|\___|_|  (_|_)
"""

RULES = """                                                                                       
    The game is played on a grid where each intersection is a "point" and
    three points in a row is called a "mill". Each player has 9 pieces and
    in Phase 1 the players take turns placing their pieces on the board to 
    make mills. When a mill (or mills) is made one opponent's piece can be 
    removed from play. In Phase 2 play continues by moving pieces to 
    adjacent points. 
    The game is ends when a player (the loser) has less than three 
    pieces on the board.
"""

MENU = """
    Game commands (first character is a letter, second is a digit):
    xx        Place piece at point xx (only valid during Phase 1 of game)
    xx yy     Move piece from point xx to point yy (only valid during Phase 2)
    R         Restart the game
    H         Display this menu of commands
    Q         Quit the game

"""

## Uncomment the following lines when you are ready to do input/output tests!
## Make sure to uncomment when submitting to Codio.
def input( prompt=None ):
    if prompt != None:
        print( prompt, end="" )
    aaa_str = sys.stdin.readline()
    aaa_str = aaa_str.rstrip( "\n" )
    print( aaa_str )
    return aaa_str


def count_mills(board, player):
    """
        Receives the game board and one of the players
        and counts the number of mills that player has
        on the board. Returns the count to the main function.
    """

    count = 0

    # If all the points in the mill are occupied by the player, increase the count by 1
    # I used the all function, but I could have also used the code block used in
    # points_not_in_mills() to find the mill count (lines 173-183) however this is a much
    # cleaner way of doing this.
    for mill in board.MILLS:
        if all(board.points[point] == player for point in mill):
            count += 1

    return count


def place_piece_and_remove_opponents(board, player, destination):
    """
        Receives the board, a player, and the destination
        the player would like to move their piece to.
        It then moves that players piece to the desired
        destination.
    """

    # Count the mills before the pice is placed
    mills_before = count_mills(board, player)

    # If the point is empty place the piece at the point
    if board.points[destination] == ' ':
        board.assign_piece(player, destination)

    # If the point is not empty rais RunTimeError message
    else:
        raise RuntimeError("Invalid command: Destination point already taken")

    # Count the mill after the piece is placed
    mills_after = count_mills(board, player)

    # If the count of mills is higher after than before, remove an opponents
    # piece from the board
    if mills_after > mills_before:
        print('A mill was formed!')
        print(board)
        opponent = get_other_player(player)
        remove_piece(board, opponent)


def move_piece(board, player, origin, destination):
    """
        Receives the game board, a player, the origin
        point of a piece, and the destination point for
        said piece.
        The function will then move the piece to the
        desired destination FROM THE PIECES ORIGINAL PLACEMENT.
    """

    # If the Origin does not belong to player: display RuntimeError
    if board.points[origin] != player:
        raise RuntimeError("Invalid command: Origin point does not belong to player")

    # If the destination is occupied already: display RuntimeError
    if board.points[destination] != ' ':
        raise RuntimeError("Invalid command: Destination point already taken")

    # If neither of the if statements execute, remove the piece at origin
    board.clear_place(origin)
    mills_before = count_mills(board, player)

    # Assign a piece at the destination
    board.assign_piece(player, destination)
    mills_after = count_mills(board, player)

    # If the mill count is higher after than before, remove opponents piece
    if mills_after > mills_before:
        print('A mill was formed!')
        print(board)
        opponent = get_other_player(player)
        remove_piece(board, opponent)

    # Check if a player has less than two remaining pieces left: if so display BANNER
    Winner = is_winner(board, player)

    if Winner:
        print(BANNER)


def points_not_in_mills(board, player): # Fix this
    """
        Receives the board and a player.
        The function then finds the points of
        pieces that are not a part of a mill
        belonging to the player.
    """
    # Create a set to hold mills that exist
    invalid_points = []

    # This could also be the all function from count_mills function (with some differences)
    # Check to see if the points form a mill, if so add the points to an invalid list
    for mill in board.MILLS:
        check = True
        for point in mill:

            if board.points[point] != player:
                check = False
                break

        if check:
            for point in mill:
                invalid_points.append(point)

    # Create a list to hold the points that are not in a mill
    valid_points = []

    # If the point is not in invalid points and the point is equal to player
    # add them to a valid list
    for point in board.points:
        if board.points[point] == player and point not in invalid_points:
            valid_points.append(point)

    return valid_points

def placed(board, player):
    """
        Receives the board and a player.
        Creates and returns a lists containing the
        points of the pieces placed by the player.
    """

    # Create a list (or set if I wasn't submitting to codio) to hold the points that hold a players piece
    point_list = []

    # If the point holds a piece, add it to the set
    for point in board.points:
        if board.points[point] == player:
            point_list.append(point)

    return point_list


def remove_piece(board, player):
    """
        Receives the board and a player.
        The function will remove a piece belonging
        to the player (When a mill is created by the
        other player).
    """

    # Get the list of players pieces from the placed function above
    player_list = placed(board, player)

    # Get the valid and invalid points from the points_not_in_mills function
    valid_points = points_not_in_mills(board, player)

    # If the player list is empty: display RuntimeError
    if not player_list:
        raise RuntimeError("Invalid command: Not a valid point")

    remove_points = True

    # While the command given is NOT valid, run this loop
    while remove_points:
        command = input('Remove a piece at :> ')

        # If the command is longer than 2: display RuntimeError
        if len(command) > 2:
            print('Invalid command: Not a valid point')
            print('Try again.')

        # If the command point does not hold the players value: display RuntimeError
        elif board.points[command] != player:
            print("Invalid command: Point does not belong to player")
            print('Try again.')

        elif command in valid_points or not valid_points:
            remove = command
            remove_points = False
            board.clear_place(remove)

        else:
            print('Invalid command: Point is in a mill')
            print('Try again.')


def is_winner(board, player):
    """
        Receives the board and a player.
        This function determines if a player
        has won by getting the other player down to
        two or fewer pieces remaining on the board.
    """

    # Set the opponent to the other player
    opponent = get_other_player(player)

    # If the player is X check if player O has less than two pieces left
    if player == 'X':
        if len(placed(board, opponent)) < 3:
            X_win = True
            return X_win

    # If the player is O check if player X has less than two pieces left
    elif player == 'O':
        if len(placed(board, opponent)) < 3:
            O_win = True
            return O_win

    return False

def reset_board(board):
    '''
        This function will receive the board
        and reset it to its original values to restart the game
    '''

    # For every point on the board, set the value to ' '
    for point in board.points:
        board.points[point] = ' '


def get_other_player(player):
    """
        The function returns the other opponent.
    """
    return "X" if player == "O" else "O"


def main():
    # Loop so that we can start over on reset
    while True:
        # Setup stuff.
        print(RULES)
        print(MENU)
        board = NMM.Board()
        print(board)
        player = "X"
        placed_count = 0  # total of pieces placed by "X" or "O", includes pieces placed and then removed by opponent

        # PHASE 1
        print(player + "'s turn!")

        # placed = 0
        command = input("Place a piece at :> ").strip().lower()
        print()

        # Until someone quits or we place all 18 pieces...
        while command != 'q' and placed_count != 18:
            try:

                # If more than 18 pieces have been placed continue to phase 2
                if placed_count < 18:

                    # If the command is 'h' display the rules and menu to the game
                    while command == 'h':
                        print(MENU)
                        command = input('Place a piece at :> ')

                    # If the command is not in the board points list, raise error message
                    if command in board.points:

                        # Place the new pieces on the board, and switch to other player
                        destination = command
                        place_piece_and_remove_opponents(board, player, destination)
                        player = get_other_player(player)
                        placed_count += 1

                    # If the command is 'r' reset the board to original form
                    elif command == 'r':
                        reset_board(board)
                        player = 'X'
                        placed_count = 0
                        print(RULES)
                        print(MENU)

                    #elif command == 'h':
                        #print(MENU)

                    # If none of the if statements iterate: display RuntimeError
                    else:
                        raise RuntimeError("Invalid command: Not a valid point")

            # Any RuntimeError you raise inside this try lands here
            except RuntimeError as error_message:
                print("{:s}\nTry again.".format(str(error_message)))
            # Prompt again
            print(board)
            print(player + "'s turn!")
            if placed_count < 18:
                command = input("Place a piece at :> ").strip().lower()
            else:
                print("**** Begin Phase 2: Move pieces by specifying two points")
                command = input("Move a piece (source,destination) :> ").strip().lower()
            print()

        # Go back to top if reset
        if command == 'r':
            continue
        # PHASE 2 of game
        while command != 'q':

            # commands should have two points
            command = command.split()
            try:

                #Old code


                # If command is 'r' reset the game (line 288 is he same)
                if command == 'r':
                    reset_board(board)
                    player = 'X'
                    print(RULES)
                    print(MENU)
                    placed_count = 0

                # If the command = 'h' display the rules and menu to the game
                elif command == 'h':
                    while command == 'h':
                        print(MENU)
                        command = input('Place a piece at :> ')


                # If the length of command is 2
                elif len(command) == 2:

                    # Assign the values of the command
                    origin, destination = command

                    # If the destination is not a point on the board: display RuntimeError
                    if destination not in board.points:
                        raise RuntimeError("Invalid command: Not a valid point")

                    # If the origin is not a point on the board: display RuntimeError
                    elif origin not in board.points:
                        raise RuntimeError("Invalid command: Origin point does not belong to player")

                    # Move the pice from origin point to destination point
                    move_piece(board, player, origin, destination)

                    if is_winner(board, player):
                        return

                    player = get_other_player(player)

                # If none of the if statements iterate: display RuntimeError
                else:
                    print('Invalid number of points')
                    print('Try again.')

            # Any RuntimeError you raise inside this try lands here
            except RuntimeError as error_message:
                print("{:s}\nTry again.".format(str(error_message)))
                # Display and reprompt
            print(board)
            # display_board(board)
            print(player + "'s turn!")
            command = input("Move a piece (source,destination) :> ").strip().lower()
            print()

        # If we ever quit we need to return
        if command == 'q':
            return

if __name__ == "__main__":
    main()
