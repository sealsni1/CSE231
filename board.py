class Ship(object):
    """
        Represents a piece in the Game.
    """
    def __init__(self, length, position, orientation) -> None:
        """
            Represent/Initialize length, position and orientation
            as arguments for the Ship Class.
        """

        self.length = length
        self.orientation = orientation
        self.hit_count = 0
        self.is_sunk = False

        self.position = list(tuple(position))

    def get_positions(self) -> list:
        """
            Returns a list of positions of the Ship.
        """

        # Create a list to hold the spaces the ship is occupying
        position = []

        # Separate the position into row and col (row, col)
        row, col = self.position

        # Determine the orientation of the ship and then add the
        # coordinates of the ship to the position list
        for i in range(self.length):
            if self.orientation == 'h':
                position.append((row, col + i))

            elif self.orientation == 'v':
                position.append((row + i, col))

        return position

    def get_orientation(self) -> str:
        """
            Returns the orientation of the ship.
        """

        return self.orientation

    def apply_hit(self) -> None:
        """
            Increases the hit_count by 1 and checks if the
            ship is sunk.
        """

        # Update the hit count for the ship
        self.hit_count += 1

        # If the hit count equals the length of the ship
        # it will sink.
        if self.hit_count == self.length:
            self.is_sunk = True


# Board Class Starts Here
class Board(object):
    """
        Represents the Board object and will keep track
        of the ships on the board, and assist with validating
        the moves made by the players.
    """
    def __init__(self, size):
        """
            Represents/Initializes size (integer) as an argument
            for the Board Class.
        """

        self.size = size
        self.board = [[' ' for i in range(size)] for j in range(size)]
        self.ships = []

    def place_ship(self, ship) -> None:
        """
            Takes the Ship object as a parameter and updates
            the ship list. It will also update the board variable with 'S'
            if said location is occupied by a ship.
        """

        # Add the ships coordinates to the ships list
        self.ships.append(ship)

        # Update Board list to 'S' for each
        # position the ships is occupying.
        for position in ship.get_positions():
            row, col = position
            self.board[row][col] = 'S'


    def apply_guess(self, guess) -> None:
        """
            Takes guess as a parameter (row, col) and
            checks if the guess landed on one of the
            opponents ships or not. If yes, updates guess
            location to 'H', else, 'M'.
        """

        # Split the guess into the appropriate groups (row, col)
        row, col = guess

        # Assign a variable to determine if a ship was hit
        hit = False

        for ship in self.ships:
            # If the guess landed on a ship, update the
            # Board to 'H' for that position.
            if guess in ship.get_positions():
                ship.apply_hit()
                hit = True
                self.board[row][col] = 'H'
                print('Hit!')
                break

        # If guess did not hit a ship, update to 'H'
        if not hit:
            self.board[row][col] = 'M'
            print('Miss!')

    def validate_ship_coordinates(self, ship) -> None:
        """
            Takes Ship object as a parameter, and checks
            if it can be placed on the current board.
        """

        # Find the ships coordinates
        for position in ship.get_positions():
            row, col = position

            # If the coordinates are not within the nXn grid
            # Raise appropriate RuntimeError.
            if not (0 <= row < self.size) and (0 <= col < self.size):
                raise RuntimeError("Ship coordinates are out of bounds!")

            # If the coordinates already have a ship occupying the space
            # Raise appropriate RuntimeError.
            if self.board[row][col] == 'S':
                raise RuntimeError("Ship coordinates are already taken!")

    def __str__(self) -> str:
        """
            Returns the current board as a readable and
            representable string the user can read.
        """

        # Assign a variable for the board string
        board_str = ''

        # For each row, col in the board list, update the
        # format and add each row to the board string
        for row in self.board:
            for col in row:
                board_str += f"[{col}]"

            board_str += "\n"

        return board_str
